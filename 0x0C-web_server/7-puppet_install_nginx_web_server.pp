# Installs a Nginx server and edit the default
package {'nginx_webserver':
    ensure      => installed,
    name        => 'nginx',
    description => 'a popular web server',
    }

file_line {'Add redirection permanently':
    ensure => present,
    path   => '/etc/nginx/sites-available/default',
    line   => 'rewrite ^ /redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
    after  => 'listen 80 default_server;',
    }

file {'index.html':
    ensure  => present,
    path    => '/var/www/html/index.html',
    content => 'Hello World!',
    }

service {'restart nginx':
    ensure => running,
    name   => 'nginx',
    }
