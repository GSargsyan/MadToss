#!/bin/bash
su
dnf install python3-devel
dnf install nginx
dnf install gcc

setenforce Enforcing
semanage permissive -a httpd_t

systemctl enable nginx.service
systemctl start nginx.service
