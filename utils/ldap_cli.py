import logging
from ldap3 import Server, Connection, ALL
from ldap3.core import exceptions

from base import errors


class LdapCli:

    def __init__(self, host, member_base_dn, admin_dn, admin_password):
        self.host = host
        self.admin_dn = admin_dn
        self.admin_password = admin_password
        self.member_base_dn = member_base_dn
        self.server = Server(self.host)

    def _create_connection(self):
        return Connection(self.server, self.admin_dn, self.admin_password, auto_bind=True)

    def get_users(self):
        '''
        获取用户列表
        '''
        dn = self.member_base_dn
        conn = self._create_connection()
        attributes = ['cn', 'sn']
        conn.search(dn, '(objectclass=person)', attributes=attributes)
        data_list = []
        for user in conn.entries:
            user = user.entry_attributes_as_dict
            data = {
                'username': user['cn'][0],
                'name': user['sn'][0],
            }
            data_list.append(data)
        return data_list

    def check_password(self, username, password):
        '''
        校验密码
        '''
        dn = f'cn={username},{self.member_base_dn}'
        try:
            Connection(self.server, dn, password, auto_bind=True)
        except exceptions.LDAPBindError as e:
            return False
        return True
