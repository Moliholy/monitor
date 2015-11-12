#!/usr/bin/env bash

set -x

cp cvmfs_web/settings.py.example cvmfs_web/settings.py
cp django.conf /etc/httpd/conf.d/django.conf

rm -rf /run/httpd/ /tmp/httpd
mkdir -p /run/httpd /tmp/httpd

touch /var/log/httpd/access_log
tail -f /var/log/httpd/access_log &
exec /usr/sbin/apachectl -DFOREGROUND

