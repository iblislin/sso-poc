from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ldap_dn = models.CharField(max_length=1024, blank=True, null=True, unique=True)

    @property
    def is_ldap(self):
        return bool(self.ldap_dn)

    #TODO: override the function `create_user` to check username in LDAP or not.
