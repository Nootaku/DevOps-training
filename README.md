# DevOps-training

## The basics
This directory is a very simple hello-world Flask-app.<br>The objective is to learn Dev-Ops basics:
- Deploy this app on a AWS EC2 instance
- Set-up a simple Nginx load-balancer / reverse proxy to port 4000
- Buy a DNS and link the IP to the DNS with Route 53
- Ensure LetsEncrypt HTTPS

## Automate everything
Once the instance is set-up, we will destroy everything and automate what we've done:
- AWS CLI + shell scripts

Destroy everything once more:
- Terraform using the AWS provider
- Ansible for instance configuration
- Docker to create an image of our Flask-app and deploy it on our server

