#!/usr/bin/env bash

# Set up SSH client configuration
file { '/etc/ssh/ssh_config':
  ensure  => file,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => "# SSH client configuration\n\
               Host *\n\
                 IdentityFile ~/.ssh/school\n\
                 PasswordAuthentication no\n",
}
