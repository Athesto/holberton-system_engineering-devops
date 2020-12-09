#create configuration file
    $str = "Host default
  HostName 35.231.13.24
  User ubuntu
  Port 22
  PasswordAuthentication no
  IdentityFile ~/.ssh/holberton
  "

    file{'/etc/ssh/ssh_config':
        content => $str,
}
