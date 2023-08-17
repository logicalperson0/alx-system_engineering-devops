#script that deals with requests failed, so that it gets to 0

exec {'no_limit':
  provider => shell,
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 2048\"/" /etc/default/nginx'
  before   => Exec['restart_nginx'],
}

exec {'restart_nginx':
  provider => shell,
  command  => 'sudo systemctl restart nginx.service',
}
