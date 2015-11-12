FROM centos:7
MAINTAINER Jose Molina <jose.molina@cern.ch>

RUN yum install epel-release -y
RUN yum update -y
RUN yum install httpd python-pip gcc git swig mod_wsgi openssl wget python-devel openssl-devel -y
RUN pip install --upgrade pip
RUN easy_install M2Crypto
RUN pip install django git+https://github.com/cvmfs/python-cvmfsutils.git

ENV workdir /opt/django-cvmfs-monitor
RUN mkdir -p $workdir /run/httpd /var/run/httpd /var/log/httpd

EXPOSE 80
EXPOSE 443

WORKDIR $workdir
ENTRYPOINT ["./deploy.sh"]
