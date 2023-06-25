#Changes SSH config file

file_line { 'Turn off passwd auth on ssh':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '  PasswordAuthentication no',
}

file_line { 'Modify identity file':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '  IdentityFile ~/.ssh/school',
}
