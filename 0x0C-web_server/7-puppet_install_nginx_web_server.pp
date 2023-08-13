# Installs a Nginx server and edit the default
package {'nginx':
    ensure => installed,
    }

file_line {'Add redirection permanently':
    ensure => present,
    path   => '/etc/nginx/sites-available/default',
    line   => 'rewrite ^ /redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
    after  => 'listen 80 default_server;',
    }

file {'index.html':
    path    => '/var/www/html/index.html',
    content => 'Hello World!',
    }

service {'nginx':
    ensure => running,
    name   => 'nginx',
    }
