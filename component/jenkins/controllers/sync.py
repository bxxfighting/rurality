from django.db import transaction
from django.db.models import Q

from component.jenkins.models import JenkinsServerModel
from component.jenkins.models import JenkinsJobModel
from base import controllers as base_ctl
from base import errors
from utils.jenkins_cli import JenkinsCli


def sync_jenkins():
    '''
    同步jenkins
    这种同步，我认为没有必要加事务
    '''
    server_objs = JenkinsServerModel.objects.all()
    old_ids = JenkinsJobModel.objects.values_list('id', flat=True).all()
    old_ids = list(set(old_ids))
    existed_ids = []
    job_list = []
    for server_obj in server_objs:
        jenkins_cli = JenkinsCli(server_obj.host, server_obj.username, server_obj.token)
        jobs = jenkins_cli.get_jobs()
        for job in jobs:
            job_name = job.get('name')
            query = {
                'server_id': server_obj.id,
                'name': job_name,
            }
            obj = JenkinsJobModel.objects.filter(**query).first()
            data = query
            data['url'] = job.get('url')
            if obj:
                base_ctl.update_obj(JenkinsJobModel, obj.id, data)
                existed_ids.append(obj.id)
            else:
                job_list.append(data)
    base_ctl.create_objs(JenkinsJobModel, job_list)
    deleted_ids = list(set(set(old_ids) - set(existed_ids)))
    if deleted_ids:
        base_ctl.delete_objs(JenkinsJobModel, deleted_ids)
