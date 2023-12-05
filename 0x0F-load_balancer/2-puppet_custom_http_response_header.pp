#!/usr/bin/env bash
# Update Ubuntu server

exec { 'update server':
  command  => 'apt-get update',
  user     => 'root',
  provider => 'shell',
}

# Install Nginx web server on the server
package { 'nginx':
  ensure   => present,
  provider => 'apt',
}

# Custom Nginx response header (X-Served-By: hostname)
file_line { 'add HTTP header':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => '    add_header X-Served-By $hostname;',
  notify => Service['nginx'],
}

# Start service
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}
