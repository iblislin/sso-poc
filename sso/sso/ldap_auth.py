from collections import namedtuple

import ldap

from django.contrib.auth.backends import BaseBackend

from sso.models import User


class FreebsdLdapBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        if request.user and not request.user.is_anonymous:
            return  # skip

        conn = ldap.initialize('ldap://localhost', bytes_mode=False)
        dn = 'uid={},dc=users,dc=demo'.format(username)

        try:
            conn.simple_bind_s(dn, password)
        except ldap.INVALID_CREDENTIALS:
            print('LDAP auth failed for {}'.format(dn))
            return

        try:
            user = User.objects.get(ldap_dn=dn)
        except User.DoesNotExist: # then create
            user = User.objects.create_user(username, ldap_dn=dn)

        query = conn.search_s(dn, scope=ldap.SCOPE_BASE)[0][1]
        conn.unbind_s()  # disconnect from LDAP server

        # update info
        user.first_name = query['cn'][0].decode('utf-8')
        user.last_name = ''
        user.email = query['mail'][0].decode('utf-8')
        user.is_staff = False
        user.is_active = True
        user.is_superuser = False
        user.save()

        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
