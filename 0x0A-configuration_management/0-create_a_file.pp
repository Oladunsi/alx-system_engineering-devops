# creating a file using puppet

file { 'school':
  ensure  => 'present',
  content => 'I love puppet',
  group   => 'www-data',
  mode    => '0744',
  owner   => 'www-data',
  path    => '/tmp/school',
}
