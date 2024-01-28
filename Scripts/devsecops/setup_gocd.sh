#!/bin/bash

# Update System Packages
sudo apt-get update

# Install Java
sudo apt-get install -y default-jre

# Add GoCD Repository
curl https://download.gocd.org/GOCD-GPG-KEY.asc | sudo apt-key add -
echo "deb https://download.gocd.org /" | sudo tee /etc/apt/sources.list.d/gocd.list

# Install GoCD Server
sudo apt-get update
sudo apt-get install -y go-server

# Start and Enable GoCD Server
sudo systemctl start go-server
sudo systemctl enable go-server

# (Optional) Install GoCD Agent
sudo apt-get install -y go-agent
sudo systemctl start go-agent
sudo systemctl enable go-agent

echo "GoCD Server installation is complete. Access it via http://<Your_Server_IP>:8153"
