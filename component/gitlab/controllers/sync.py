from django.db import transaction
from django.db.models import Q

from component.gitlab.models import GitlabServerModel
from component.gitlab.models import GitlabProjectModel
from base import controllers as base_ctl
from base import errors
from utils.gitlab_cli import GitlabCli


def sync_gitlabs():
    '''
    同步gitlab
    这种同步，我认为没有必要加事务
    '''
    # 虽然我说我不建议有多个代码库，但是我写代码肯定是要支持多个的，因为并没有增加多少工作量
    server_objs = GitlabServerModel.objects.all()
    old_ids = GitlabProjectModel.objects.values_list('id', flat=True).all()
    old_ids = list(set(old_ids))
    existed_ids = []
    project_list = []
    for server_obj in server_objs:
        gitlab_cli = GitlabCli(server_obj.host, server_obj.token)
        projects = gitlab_cli.get_projects()
        for project in projects:
            project_id = project.id
            query = {
                'server_id': server_obj.id,
                'project_id': project_id,
            }
            obj = GitlabProjectModel.objects.filter(**query).first()
            data = query
            data['name'] = project.path_with_namespace
            data['web_url'] = project.web_url
            data['ssh_url'] = project.ssh_url_to_repo
            if obj:
                base_ctl.update_obj(GitlabProjectModel, obj.id, data)
                existed_ids.append(obj.id)
            else:
                project_list.append(data)
    base_ctl.create_objs(GitlabProjectModel, project_list)
    deleted_ids = list(set(set(old_ids) - set(existed_ids)))
    if deleted_ids:
        base_ctl.delete_objs(GitlabProjectModel, deleted_ids)
