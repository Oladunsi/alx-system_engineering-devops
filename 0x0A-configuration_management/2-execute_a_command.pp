# command to kill a program using puppet

exec { 'killmenow':
  command => 'pkill killmenow',
  path    => '/usr/bin/'
}
