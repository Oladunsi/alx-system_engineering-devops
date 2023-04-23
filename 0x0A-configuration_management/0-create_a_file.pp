# creating a file using puppet in /tmp 

file { 'tmp/school':
  ensure  => 'file',
  content => 'I love puppet',
  group   => 'www-data',
  mode    => '0744',
  owner   => 'www-data',
  path    => '/tmp/school',
}
