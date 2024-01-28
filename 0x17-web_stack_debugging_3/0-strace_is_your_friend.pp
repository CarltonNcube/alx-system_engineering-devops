# Puppet manifest to fix PHP extension issue

exec { 'settingPress':
  command  => 'sed -i "s/\b.phpp\b/.php/g" /var/www/html/wp-settings.php',
  provider => shell,
