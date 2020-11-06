from django.core.management.base import BaseCommand
from django.urls.resolvers import URLPattern
from django.urls.resolvers import URLResolver

from rurality.urls import urlpatterns
from account.models import PermissionModel
from base import controllers as base_ctl


class Command(BaseCommand):
    '''
    同步URL到权限
    '''

    def handle(self, *args, **options):
        urls = self.get_all_urls()
        data_list = []
        for url in urls:
            if PermissionModel.objects.filter(sign=url).exists():
                continue
            data = {
                'name': 'name',
                'sign': url,
                'typ': PermissionModel.TYP_OP,
                'rank': 0
            }
            data_list.append(data)
        base_ctl.create_objs(PermissionModel, data_list)

    def get_all_urls(self):
        sub_urls = []
        for urlpattern in urlpatterns:
            sub_urls += self.get_sub_urls(urlpattern)
        # 这里我把所有url开头加上了斜线，如果没有这个需求可以不用
        urls = ['/' + sub_url for sub_url in sub_urls]
        return urls

    def get_sub_urls(self, urlpattern):
        url = urlpattern.pattern.describe().replace('\'', '')
        # 如果是URLPattern，就说明到最后一层了，直接返回url就可以，但是需要返回列表结构
        if isinstance(urlpattern, URLPattern):
            return [url]
        elif isinstance(urlpattern, URLResolver):
            sub_urls = []
            for p in urlpattern.url_patterns:
                sub_urls += self.get_sub_urls(p)
            urls = [url + sub_url for sub_url in sub_urls]
            return urls
