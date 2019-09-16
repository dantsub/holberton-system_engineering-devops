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

## 7-file

~~~
~~~

This script creates a file named exactly \*\\'"Holberton School"\'\\*$\?\*\*\*\*\*:) containing the text Holberton School ending by a new line.

## 8-cwd_state

~~~
~~~

This script  writes into the file ls_cwd_content the result of the command ls -la. If the file ls_cwd_content already exists, it should be overwritten. If the file ls_cwd_content does not exist, create it.

## 9-duplicate_last_line

~~~
~~~

This script duplicates the last line of the file iacta.

## 10-no_more_js

~~~
~~~

This script deletes all the regular files (not the directories) with a .js extension that are present in the current directory and all its subfolders.

## 11-directories

~~~
~~~

This script counts the number of directories and sub-directories in the current directory.

- The current and parent directories should not be taken into account
- Hidden directories should be counted

## 12-newest_files

~~~
~~~

This script displays the 10 newest files in the current directory.

## 13-unique

~~~
~~~

This takes a list of words as input and prints only words that appear exactly once.

- Input format: One line, one word
- Output format: One line, one word
- Words should be sorted

## 14-findthatword

~~~
~~~

This script display lines containing the pattern root from the file /etc/passwd

## 15-countthatword

~~~
~~~

This script display the number of lines that contain the pattern bin in the file /etc/passwd

## 16-whatsnext

~~~
~~~

This script display lines containing the pattern root and 3 lines after them in the file.

## 17-hidethisword

~~~
~~~

This script display all the lines in the file /etc/passwd that do not contain the pattern bin.

## 18-letteronly

~~~
~~~

This script display all lines of the file /etc/ssh/sshd_config starting with a letter.

- include capital letters as well

## 19-AZ

~~~
~~~

This script replace all characters A and c from input to Z and e respectively.

## 20-hiago

~~~
~~~

This script removes all letters c and C from input.

## 21-reverse

~~~
~~~

This script reverse its input.

## 22-users_and_homes

~~~
~~~

This script displays all users and their home directories, sorted by users.
