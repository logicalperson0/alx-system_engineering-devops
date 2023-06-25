#Changes SSH config file
exec { 'echo':
    ensure   => present,
    path     => 'usr/bin:/bin',
    command  => 'echo "    PasswordAuthentication no         ssh-copy-id -f ~/.ssh/school ubuntu@100.26.250.214" >> /etc/ssh/ssh_config',
    provider => 'shell',
    }
