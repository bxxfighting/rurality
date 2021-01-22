from django.db import transaction
from django.db.models import Q

from component.jenkins.models import JenkinsJobModel
from scheduler.controllers import berry as berry_ctl
from base import controllers as base_ctl
from base import errors


def get_jenkins_jobs(server_id=None, keyword=None, page_num=None, page_size=None, operator=None):
    '''
    获取Jenkins Job列表
    '''
    base_query = JenkinsJobModel.objects
    if server_id:
        base_query = base_query.filter(server_id=server_id)
    if keyword:
        base_query = base_query.filter(Q(name__icontains=keyword) |
                                       Q(url__icontains=keyword))
    total = base_query.count()
    objs = base_ctl.query_objs_by_page(base_query, page_num, page_size)
    data_list = []
    for obj in objs:
        data = obj.to_dict()
        data_list.append(data)
    data = {
        'total': total,
        'data_list': data_list,
    }
    return data


def sync_jenkins_jobs(operator=None):
    '''
    同步代码库
    '''
    params = {}
    data = {
        'name': '同步Jenkins Job',
        'typ': 'sync_jenkins',
        'params': params,
    }
    berry_ctl.create_berry(**data)
