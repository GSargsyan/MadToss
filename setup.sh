#!/bin/bash
su
dnf install python3-devel
dnf install nginx
dnf install gcc
dnf install python3-flask
dnf install uwsgi
dnf install uwsgi-plugin-python3
dnf install postgresql-server
dnf install postgresql-contrib
dnf install pgadmin3

python -m pip install passlib

setenforce Enforcing
semanage permissive -a httpd_t

systemctl enable postgresql
systemctl start postgresql
postgresql-setup --initdb --unit postgresql

systemctl enable nginx.service
systemctl start nginx.service

# Running uWSGI
# uwsgi --ini /var/www/MadToss/configs/uwsgi.ini

# sudo -u postgres

# to kill uWSGI proc 
# lsof -i:8080
# kill PID
