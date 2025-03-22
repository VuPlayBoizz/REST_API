#! /bin/bash
cd /home/ubuntu
sudo apt update -y
sudo apt install python3 python3-pip -y
git clone https://github.com/VuPlayBoizz/REST_API.git
sleep 50
cd REST_API
pip3 install -r requirements.txt
