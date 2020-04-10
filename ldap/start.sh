set -x

service rsyslog start

slapadd -v -n 0 -F /etc/ldap/slapd.d/ -l /opt/ldap/slapd.ldif
chown -R openldap:openldap /etc/ldap/slapd.d/
service slapd start
sleep 1

if [ ! -f /var/lib/ldap/data.mdb ]
then
    ldapadd -H 'ldap:///' -x -D "cn=admin,dc=demo" -w "secret" -f /opt/ldap/base.ldif
fi

tail -f /var/log/slapd.log
