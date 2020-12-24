from django.db import transaction
from django.db.models import Q

from asset.slb.models import SlbModel
from asset.domain.models import DomainRecordAssetModel
from base import controllers as base_ctl
from base import errors


def get_slb_domains(obj_id, page_num=None, page_size=None, operator=None):
    '''
    获取SLB解析到的域名
    '''
    query = {
        'asset_obj_id': obj_id,
        'typ': DomainRecordAssetModel.TYP_SLB,
    }
    base_query = DomainRecordAssetModel.objects.filter(**query)
    total = base_query.count()
    objs = base_ctl.query_objs_by_page(base_query, page_num, page_size)
    data_list = []
    for obj in objs:
        data = obj.to_dict()
        data['domain'] = obj.record.to_dict()
        data_list.append(data)
    data = {
        'total': total,
        'data_list': data_list,
    }
    return data
