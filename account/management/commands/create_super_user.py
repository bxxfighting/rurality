from django.core.management.base import BaseCommand

from account.controllers import user as user_ctl


class Command(BaseCommand):
    '''
    创建超级管理员账户
    '''

    def add_arguments(self, parser):
        parser.add_argument('password')

    def handle(self, *args, **options):
        password = options['password']
        user_ctl.create_user('admin', password, '超级管理员')
