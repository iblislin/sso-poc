FROM ubuntu:18.04

ENV LDAP_ADMIN_PASSWORD magic
ENV DEBIAN_FRONTEND noninteractive

# Fix apt ipv6 update issue
RUN echo 'precedence ::ffff:0:0/96 100' > /etc/gai.conf
RUN sed --in-place --regexp-extended "s/(\/\/)(archive\.ubuntu)/\1tw.\2/" /etc/apt/sources.list
RUN apt update

RUN apt install -y ldap-utils slapd rsyslog

RUN echo 'SLAPD_SERVICES="ldap:/// ldapi:/// ldaps:///"' > /etc/default/slapd

WORKDIR /opt/ldap

COPY ./slapd.ldif .
COPY ./base.ldif .
COPY ./nis.ldif .
COPY ./10-slapd.conf /etc/rsyslog.d/
COPY ./start.sh /opt/start.sh

RUN rm -vr /etc/ldap/slapd.d/* /var/lib/ldap/*

CMD sh /opt/start.sh
