#Changes SSH config file
file_line { 'passwd off in ssh':
    ensure => present,
    path   => '/etc/ssh/ssh_config',
    line   => ' PasswordAuthentication no',
    }
file_line {'modify Identity file':
    ensure => present.
    path   => '/etc/ssh/ssh_config',
    line   => ' IdentityFile ~/.ssh/school',
    }
