# Shell, I/O Redirections and filters

## 0-hello_world

~~~
#!/bin/bash
echo "Hello, World"
~~~

This script print "Hello, World".

## 1-confused_smiley

~~~
#!/bin/bash
echo \""(Ôo)'"
~~~

This script display a confused smiley "(Ôo)'

## 2-hellofile

~~~
cat /etc/passwd
~~~

This script display the content of the /etc/passwd file.

## 3-twofiles

~~~
cat /etc/passwd /etc/hosts
~~~

This script display the content of /etc/passwd and /etc/hosts

## 4-lastlines

~~~
tail /etc/passwd
~~~

This script display the last 10 lines of /etc/passwd

## 5-firstlines

~~~
head /etc/passwd
~~~

This script display the last 10 lines of /etc/passwd

## 6-third_line

~~~
head -n 3 iacta
~~~

This script displays the third line of the file iacta.


