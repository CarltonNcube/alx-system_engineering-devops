#!/usr/bin/pup

# Declare a package resource
package { 'flask':
  # Ensure the package is installed with the specified version
  ensure   => '2.1.0',
  # Use pip3 as the provider to install the package
  provider => 'pip3'
}
