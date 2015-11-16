#!/usr/bin/env bash

rm -f cvmfs_web/settings.py
cp cvmfs_web/settings.py.example cvmfs_web/settings.py

rm -rf /run/httpd/ /tmp/httpd
mkdir -p /run/httpd /tmp/httpd

python manage.py collectstatic --noinput
chown -R apache /var/www/html

exec /usr/sbin/apachectl -DFOREGROUND