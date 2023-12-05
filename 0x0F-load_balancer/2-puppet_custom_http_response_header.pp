#!/usr/bin/env bash

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Get the server hostname
$hostname = $facts['hostname']

# Create an Nginx configuration file with the custom header
file { '/etc/nginx/conf.d/custom_header.conf':
  ensure  => present,
  content => "add_header X-Served-By ${hostname};",
  require => Package['nginx'],
}

# Restart Nginx service to apply changes
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/conf.d/custom_header.conf'],
}
