#Changes SSH config file
file_line { 'passwd off and copy pub key':
    ensure => present,
    path   => '/etc/ssh/ssh_config',
    line   => 'PasswordAuthentication no',
    }
file_line {'ssh copy id':
    ensure => present.
    path   => '/etc/ssh/ssh_config',
    line   => 'ssh-copy-id -f ~/.ssh/school ubuntu@100.26.250.214',
    }
