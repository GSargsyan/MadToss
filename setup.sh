#!/bin/bash
su
dnf install python3-devel
dnf install nginx
dnf install gcc
dnf install python3-flask

setenforce Enforcing
semanage permissive -a httpd_t

systemctl enable nginx.service
systemctl start nginx.service

# Running uWSGI
# uwsgi --socket 0.0.0.0 --protocol=http -w wsgi --daemonize uwsgi.log
# uwsgi --ini /var/www/MadToss/configs/uwsgi.ini

# to kill uWSGI proc 
# isof -i:8080
# kill PID
