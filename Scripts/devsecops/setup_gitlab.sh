#!/bin/bash

# Update System
yum update -y
yum upgrade -y

# Install Required Packages
dnf -y install curl vim policycoreutils python3-policycoreutils git

# Add GitLab CE Repository
echo '[gitlab_gitlab-ce]
name=gitlab_gitlab-ce
baseurl=https://packages.gitlab.com/gitlab/gitlab-ce/el/8/$basearch
repo_gpgcheck=1
gpgcheck=1
enabled=1
gpgkey=https://packages.gitlab.com/gitlab/gitlab-ce/gpgkey https://packages.gitlab.com/gitlab/gitlab-ce/gpgkey/gitlab-gitlab-ce-3D645A26AB9FBD22.pub.gpg
sslverify=1
sslcacert=/etc/pki/tls/certs/ca-bundle.crt
metadata_expire=300

[gitlab_gitlab-ce-source]
name=gitlab_gitlab-ce-source
baseurl=https://packages.gitlab.com/gitlab/gitlab-ce/el/8/SRPMS
repo_gpgcheck=1
gpgcheck=1
enabled=1
gpgkey=https://packages.gitlab.com/gitlab/gitlab-ce/gpgkey https://packages.gitlab.com/gitlab/gitlab-ce/gpgkey/gitlab-gitlab-ce-3D645A26AB9FBD22.pub.gpg
sslverify=1
sslcacert=/etc/pki/tls/certs/ca-bundle.crt
metadata_expire=300' > /etc/yum.repos.d/gitlab_gitlab-ce.repo

# Verify Repository
dnf repolist

# Install GitLab CE
dnf install gitlab-ce -y

# Configure GitLab
vim /etc/gitlab/gitlab.rb  # Manually set external_url
sudo ln -sf /usr/lib64/libcrypt.so.2 /usr/lib64/libcrypt.so.1
gitlab-ctl reconfigure

# Allow Ports on Firewall
firewall-cmd --permanent --zone=public --add-service=http
firewall-cmd --permanent --zone=public --add-service=https
firewall-cmd --reload

# Access GitLab
echo "Access GitLab at your domain. Initial password can be found at /etc/gitlab/initial_root_password"