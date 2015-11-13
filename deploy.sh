#!/usr/bin/env bash

cp cvmfs_web/settings.py.example cvmfs_web/settings.py

rm -rf /run/httpd/ /tmp/httpd
mkdir -p /run/httpd /tmp/httpd

exec /usr/sbin/apachectl -DFOREGROUND
