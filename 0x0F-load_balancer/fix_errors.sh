#!/bin/bash

NGINX_CONFIG="/etc/nginx/sites-available/default"

# Remove duplicate entries in the Nginx configuration file
sudo sed -i '/add_header X-Served-By/d' "$NGINX_CONFIG"

# Add the add_header directive to the Nginx configuration file
sudo sed -i '/listen 80 default_server;/a \\\tadd_header X-Served-By $hostname;' "$NGINX_CONFIG"

# Check Nginx configuration for syntax errors
nginx_test_output=$(sudo nginx -t 2>&1)

# If there are syntax errors, print the errors and exit
if [[ "$nginx_test_output" =~ "syntax is okay" ]]; then
    echo "Nginx configuration syntax is OK."
else
    echo "Error in Nginx configuration syntax:"
    echo "$nginx_test_output"
    exit 1
fi

# Restart Nginx
sudo systemctl restart nginx

echo "Errors fixed. Nginx restarted successfully."
