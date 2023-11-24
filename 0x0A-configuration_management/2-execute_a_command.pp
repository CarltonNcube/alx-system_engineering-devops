#!/usr/bin/pup

# Declare an exec resource
exec { 'killmenow':
  # Use pkill to kill the process by name
  command => 'pkill killmenow',
  # Only run the command if the process is running
  onlyif  => 'pgrep killmenow',
  # Set the path to find the pkill and pgrep commands
  path    => ['/usr/bin', '/bin'],
}
