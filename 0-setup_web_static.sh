#!/usr/bin/env bash
#Install nginx if not already installed
sudo apt-get update
sudo apt-get install -y nginx

#create directories
sudo mkdir -p /data/web_static/{releases/test,shared}
echo "This is a test file to test nginx configuration" | sudo tee /data/web_static/releases/test/index.html

#create symbolic link
sudo rm -rf /data/web_static/current
sudo ln -sf /data/web_static/releases/test /data/web_static/current

#Give ownership of /data/ to ubuntu
sudo chown -R ubuntu:ubuntu /data/

#update nginx config
config_file="/etc/nginx/sites-available/default"
sudo sed -i 's|server_name _;|server_name _;\n\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n|' $config_file

#Restart nginx
sudo service nginx restart
