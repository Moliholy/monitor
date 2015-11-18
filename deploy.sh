#!/usr/bin/env bash

set -e

SCRIPT_DIR=$( cd $(dirname $0) ; pwd -P )
cd "$SCRIPT_DIR"

rm -f cvmfs_web/settings.py
cp cvmfs_web/settings.py.example cvmfs_web/settings.py

rm -rf /run/httpd/ /tmp/httpd
mkdir -p /run/httpd /tmp/httpd

python manage.py collectstatic --noinput

exec /usr/sbin/apachectl -DFOREGROUND