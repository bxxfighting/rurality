import re
import jenkins
import requests
import ujson as json
from requests.auth import HTTPBasicAuth
from utils import time_utils


class JenkinsCli:
    '''
    Jenkins操作类
    此功能主要依赖pip install python-jenkins
    因为这个库有些功能并没有实现，因此还抓取了jenkins的一些别的接口
    这些接口需要自己增加验证功能，self.auth就是
    '''

    def __init__(self, host, username, token):
        self.host = host
        self.username = username
        self.token = token
        self.server = jenkins.Jenkins(self.host, username=self.username, password=self.token)
        self.auth = HTTPBasicAuth(username, self.token)

    def get_views(self):
        '''
        获取所有view
        '''
        views = self.server.get_views()
        return views

    def get_jobs(self, view_name=None):
        '''
        获取所有job，指定了view名称，就是获取指定view下的job
        '''
        jobs = self.server.get_jobs(view_name=view_name)
        return jobs

    def run_job(self, job_name, d_param):
        '''
        运行job，指定job名称及参数
        d_param: 参数dict
        '''
        return self.server.build_job(job_name, d_param)

    def get_job_info(self, job_name):
        '''
        获取job信息
        '''
        data = self.server.get_job_info(job_name)
        return data

    def get_job_build_info(self, job_name, build_number):
        '''
        获取job构建信息
        '''
        try:
            data = self.server.get_build_info(job_name, build_number)
        except jenkins.JenkinsException as e:
            data = None
        return data

    def get_next_build_number(self, job_name):
        '''
        获取job下次构建号
        '''
        return self.server.get_job_info(job_name)['nextBuildNumber']

    def job_exists(self, job_name):
        '''
        判断job是否存在
        '''
        return self.server.job_exists(job_name)

    def _get_queue_info(self, queue_number):
        '''
        使用队列号，获取队列信息
        '''
        return self.server.get_queue_item(queue_number)

    def queue_number_to_build_info(self, queue_number):
        '''
        队列号获取构建信息
        '''
        data = self._get_queue_info(queue_number)
        build_info = {}
        # 当开始执行或在队列时被取消，会存在executable字段和cancelled字段
        if 'executable' in data.keys():
            executable = data.get('executable')
            cancelled = data.get('cancelled')
            build_info['cancelled'] = cancelled
            if not cancelled:
                build_info['build_number'] = executable.get('number')
                build_info['build_url'] = executable.get('url')
        return build_info


    def get_job_build_output(self, job_name, build_number):
        '''
        获取job构建输出
        这里根据pipeline的输出格式进行了一些处理
        其实我是觉得一大坨直接显示就不错，跟jenkins本身output一样
        '''
        output = self.server.get_build_console_output(job_name, build_number)
        output = output.replace('\\n', '\n')
        stages = output.split('[Pipeline] stage')
        stage_list = []
        for stage in stages:
            lines = stage.split('\n')
            lines = [line.strip() for line in lines if line.strip() != '']
            title = re.match(r'\[Pipeline\] { \((.*?)\)', lines[0])
            if not title:
                continue
            title = title.group(1)
            lines = [line for line in lines if line.find('[Pipeline]') == -1]
            stage_list.append({
                'title': title,
                'output': lines
            })
        return stage_list

    def _get_job_build_stages(self, job_name, build_number):
        '''
        获取构建节点列表
        这是抓取jenkins本身的接口后，实现的功能
        在jenkins上，可以显示各种阶段执行的时间等信息
        因为通过抓取是此接口，所以实现一下对应功能
        '''
        url = "/blue/rest/organizations/jenkins/pipelines/{}/runs/{}/nodes/?limit=10000".format(job_name, build_number)
        url = self.host + url
        try:
            res = requests.get(url, auth=self.auth)
            data_list = json.loads(res.content)
        except:
            data_list = []
        stages = []
        for data in data_list:
            dt_start = ''
            if data.get('startTime'):
                dt_start = time_utils.str2datetime_by_format(data.get('startTime'), '%Y-%m-%dT%H:%M:%S.%f+0800')
                dt_start = time_utils.datetime2str_by_format(dt_start)
            stage = {
                'id': data.get('id'),
                'name': data.get('displayName'),
                'result': data.get('result'),
                'state': data.get('state'),
                'dt_start': dt_start,
                'duration': data.get('durationInMillis'),
                'type': data.get('type'),
            }
            stages.append(stage)
        return stages

    def _get_job_build_stage_steps(self, job_name, build_number, node_id):
        '''
        在jenkins中信息是分层级的，job -> build -> stage -> step -> log
        这里是获取某一stage下所有step
        '''
        url = "/blue/rest/organizations/jenkins/pipelines/{}/runs/{}/nodes/{}/steps/".\
                format(job_name, build_number, node_id)
        url = self.host + url
        try:
            res = requests.get(url, auth=self.auth)
            data_list = json.loads(res.content)
        except:
            data_list = []
        steps = []
        for data in data_list:
            dt_start = ''
            if data.get('startTime'):
                dt_start = time_utils.str2datetime_by_format(data.get('startTime'), '%Y-%m-%dT%H:%M:%S.%f+0800')
                dt_start = time_utils.datetime2str_by_format(dt_start)
            step = {
                'id': data.get('id'),
                'name': data.get('displayName'),
                'result': data.get('result'),
                'state': data.get('state'),
                'dt_start': dt_start,
                'duration': data.get('durationInMillis'),
                'type': data.get('type'),
            }
            steps.append(step)
        return steps

    def _get_job_build_stage_step_log(self, job_name, build_number, node_id, step_id):
        '''
        获取step下的日志
        '''
        url = "/blue/rest/organizations/jenkins/pipelines/{}/runs/{}/nodes/{}/steps/{}/log/".\
                format(job_name, build_number, node_id, step_id)
        url = self.host + url
        try:
            res = requests.get(url, auth=self.auth)
            log = res.content.decode()
        except:
            log = ''
        log = log.replace('\r\n', '\n')
        return log

    def get_job_build_detail(self, job_name, build_number):
        '''
        按照构建阶段组织信息
        '''
        stages = self._get_job_build_stages(job_name, build_number)
        stage_data_list = []
        for stage in stages:
            stage_id = stage.get('id')
            stage_data = stage
            steps = self._get_job_build_stage_steps(job_name, build_number, stage_id)
            step_data_list = []
            for step in steps:
                step_id = step.get('id')
                step_data = step
                log = self._get_job_build_stage_step_log(job_name, build_number, stage_id, step_id)
                step_data['log'] = log
                step_data_list.append(step_data)
            stage_data['steps'] = step_data_list
            stage_data_list.append(stage_data)
        return stage_data_list
