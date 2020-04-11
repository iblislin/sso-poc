set -x

service rsyslog start

slapadd -v -n 0 -F /etc/ldap/slapd.d/ -l /opt/ldap/slapd.ldif
chown -R openldap:openldap /etc/ldap/slapd.d/
service slapd start
sleep 1

ldapadd -H 'ldap:///' -x -D "cn=admin,dc=demo" -w "secret" -f /opt/ldap/base.ldif

tail -f /var/log/slapd.log
