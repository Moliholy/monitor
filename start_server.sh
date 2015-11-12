#!/usr/bin/env bash

SCRIPT_DIR=$( cd $(dirname $0) ; pwd -P )

docker build -t monitor "$SCRIPT_DIR"
docker run -p 80:80 -p 443:443 -v "$SCRIPT_DIR":/opt/django-cvmfs-monitor:rw monitor