#create configuration file
    $str = "Host default
  HostName 35.231.13.24
  User ubuntu
  Port 22
  PasswordAuthentication no
  IdentityFile /home/vagrant/.ssh/holberton
  "
    $mypath = '/home/vagrant/.ssh/config'

    file{'2-ssh_config':
        path    => $mypath,
        content => $str,
}
