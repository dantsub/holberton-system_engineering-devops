# install and configure an Nginx server using Puppet instead of Bash

package { 'nginx':
  ensure  => installed,
  name    => 'nginx',
}

file { '/var/www/html/index.html':
  path    => '/var/www/html/index.html',
  content => 'Holberton School',
}

file_line { 'title':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  after  => 'server_name _;',
  line   => 'location /redirect_me {\n\treturn 301 https://www.holbertonschool.com/co;\n}',
  match  => '^location / {',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
