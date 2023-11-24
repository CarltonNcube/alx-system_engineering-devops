#!/usr/bin/pup

# Declare a file resource
file { '/tmp/school':
  # Ensure the file exists
  ensure  => 'file',
  # Set the file mode to 0744 (owner can read, write, and execute; group and others can only read)
  mode    => '0744',
  # Set the file owner to www-data
  owner   => 'www-data',
  # Set the file group to www-data
  group   => 'www-data',
  # Set the file content to 'I love Puppet'
  content => 'I love Puppet',
}
