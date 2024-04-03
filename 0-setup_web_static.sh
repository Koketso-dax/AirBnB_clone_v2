#!/usr/bin/env bash
# Install Nginx if not already installed
sudo apt-get update
sudo apt-get -y install nginx

# Create necessary directories
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# Create a fake HTML file
sudo touch /data/web_static/releases/test/index.html
sudo bash -c 'cat > /data/web_static/releases/test/index.html' << EOF
<html>
<head></head>
<body>Holberton School</body>
</html>
EOF

# Create or recreate symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Set ownership recursively to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

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

sudo bash -c 'cat > /etc/nginx/sites-enabled/default' << EOF
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

sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/; }' "/etc/nginx/sites-enabled/default"

# Restart Nginx
sudo service nginx restart
