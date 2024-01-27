# Puppet manifest to fix the PHP extension issue in wp-settings.php

exec { 'fix the php extension issue':
    command => 'sed -i "s/php/phpp/g" /var/www/html/wp-settings.php',
    path    => '/usr/local/bin/:/bin/'
}
