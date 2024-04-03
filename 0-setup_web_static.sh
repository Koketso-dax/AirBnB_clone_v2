#!/usr/bin/env bash
# Install Nginx if not already installed
sudo apt-get update
sudo apt-get install nginx -y
sudo ufw allow 'Nginx HTTP'
# Create necessary directories
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# Create a fake HTML file
sudo bash -c 'cat > /data/web_static/releases/test/index.html' << EOF
<html>
<head></head>
<body>Holberton School</body>
</html>
EOF

# Create or recreate symbolic link
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

# Set ownership recursively to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Remove existing symbolic link if it exists
sudo rm -f /etc/nginx/sites-enabled/default

# Configure a default setup
sudo bash -c 'cat > /etc/nginx/sites-available/default' << EOF
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    server_name _;

    add_header X-Served-By \$hostname;

    location / {
        try_files \$uri \$uri/ =404;
    }

    location /hbnb_static {
        alias /data/web_static/current/;
    }
}
EOF

# Create symbolic link to Nginx configuration file
sudo ln -sf /etc/nginx/sites-available/default /etc/nginx/sites-enabled/

# Restart Nginx
sudo service nginx restart
