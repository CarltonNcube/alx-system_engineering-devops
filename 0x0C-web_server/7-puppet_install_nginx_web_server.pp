#!/usr/bin/env bash

# nginx_config.pp

# Install Nginx package
package { 'nginx':
  ensure => present,
}

# Configure Nginx
file { '/etc/nginx/sites-available/default':
  ensure => present,
  source => 'puppet:///modules/nginx_config/nginx_default',
  notify => Service['nginx'],
}

file { '/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World!',
}

file { '/etc/nginx/sites-available/redirect_me':
  ensure => present,
  source => 'puppet:///modules/nginx_config/nginx_redirect_me',
  notify => Service['nginx'],
}

file { '/etc/nginx/sites-enabled/redirect_me':
  ensure => link,
  target => '/etc/nginx/sites-available/redirect_me',
  notify => Service['nginx'],
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

# nginx_default template
file { '/etc/nginx/sites-available/default':
  ensure => present,
  content => template('nginx_config/nginx_default.erb'),
}

# nginx_redirect_me template
file { '/etc/nginx/sites-available/redirect_me':
  ensure => present,
  content => template('nginx_config/nginx_redirect_me.erb'),
}
