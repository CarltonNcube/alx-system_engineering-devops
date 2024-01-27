# Puppet manifest to fix PHP extension issue

exec { 'fix-wordpress':
    command => 'sed -i "s/php/phpp/g" /var/www/html/wp-settings.php',
    path    => '/usr/local/bin/:/bin/'
}
