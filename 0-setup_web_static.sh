#!/usr/bin/env bash

# Install Nginx if not already installed
sudo apt-get update
sudo apt-get -y install nginx

# Create necessary directories
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
sudo mkdir -p /data/web_static/current

# Create a fake HTML file
sudo touch /data/web_static/releases/test/index.html
sudo bash -c 'echo "<html><head></head><body>Holberton School</body></html>" > /data/web_static/releases/test/index.html'

# Create or recreate symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Set ownership recursively to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve content to hbnb_static
nginx_config="/etc/nginx/sites-enabled/default"
nginx_config_backup="/etc/nginx/sites-enabled/default.bak"
if [ ! -f "$nginx_config_backup" ]; then
    sudo cp "$nginx_config" "$nginx_config_backup"
fi

sudo bash -c 'echo "server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    server_name koketsodiale.tech www.koketsodiale.tech;

    location / {
        try_files \$uri \$uri/ =404;
    }

    location /hbnb_static {
        alias /data/web_static/current/;
    }
}" > "$nginx_config"'

sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/; }' "$nginx_config"

# Restart Nginx
sudo service nginx restart
