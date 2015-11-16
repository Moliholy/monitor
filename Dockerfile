FROM centos:7
MAINTAINER Jose Molina <jose.molina@cern.ch>

RUN yum install epel-release -y
RUN yum update -y
RUN yum install httpd python-pip gcc git swig mod_wsgi openssl wget python-devel openssl-devel -y
RUN pip install --upgrade pip
RUN easy_install M2Crypto
RUN pip install django git+https://github.com/cvmfs/python-cvmfsutils.git git+https://github.com/cvmfs/cvmfs-browser.git

RUN mkdir -p /opt/django-cvmfs-monitor /run/httpd /var/run/httpd /var/log/httpd
COPY django.conf /etc/httpd/conf.d/django.conf

EXPOSE 80
EXPOSE 443

WORKDIR /opt/django-cvmfs-monitor
