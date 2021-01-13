import gitlab
from gitlab.exceptions import GitlabGetError


class GitlabCli:

    def __init__(self, host, private_token):
        self.gl = gitlab.Gitlab(host, private_token=private_token)

    def get_projects(self, keyword=None):
        '''
        获取项目列表，可通过关键字搜索，或者全量返回
        '''
        if keyword:
            return self.gl.projects.list(search=keyword)
        else:
            return self.gl.projects.list(all=True)

    def get_project(self, project_id):
        '''
        获取单个项目信息
        ps: 这里错误处理其实是扯淡的<!x!<
        '''
        try:
            project = self.gl.projects.get(project_id)
        except GitlabGetError as e:
            raise errors.CommonError('gitlab中不存在此项目')
        return project

    def get_project_branches(self, project_id):
        '''
        获取项目下分支列表
        分支还要分页?搜索？请删删分支吧
        '''
        project = self.get_project(project_id)
        branches = project.branches.list(all=True)
        branches = [obj.name for obj in branches]
        return branches

    def get_project_tags(self, project_id, keyword=None, page_num=1, page_size=10):
        '''
        获取项目下tag列表
        '''
        project = self.get_project(project_id)
        if keyword:
            tags = project.tags.list(search=keyword, page=page_num, per_page=page_size)
        else:
            tags = project.tags.list(page=page_num, per_page=page_size)
        tags = [obj.name for obj in tags]
        return tags
