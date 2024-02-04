#!/usr/bin/env bash
#Install Nginx if it not already installed

apt-get update
apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
touch /data/web_static/releases/test/index.html
echo "<html>
  <head>
  </head>
  <body>
    <h1>Welcome in WOLVROK</h1>
    <P> Developed by MrMD</P>
  </body>
</html>" > /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i ' 7 i \\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default
sudo service nginx restart
