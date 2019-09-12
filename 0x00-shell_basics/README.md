# SHELL BASICS

## pwd

This commad is for print absolute path name of the current working directory.

## ls

This command is for display the contents list of the current directory.

## cd ~

This is the command that changes the working directory to the user's home directory.

## ls -l

This command display current directory contents in a long format.

## ls -s -l

This command display current directory contents, including hidden files and a long format.

## ls -la -n

This command display current directory contens.

## mkdir /tmp/holberton

This commad is for creates a directory in /tmp/ directory.

## mv /tmp/betty /tmp/holberton/betty

This command is for move betty in holberton.

## rm /tmp/holberton/betty

This command is for remove file betty from /tmp/holberton/.

## rm -r /tmp/holberton

This command is for remove directory holberton from /tmp/.

## cd - 

This command that change the working directory to the previous one.

## ls -l . .. /boot

This command that lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the /boot directory (in this order), in long format.

## file /tmp/iamafile

This is for prints the type of the file named iamafile from /tmp/.

## ln -s /bin/ls __ls__

This command is for Create a symbolic link to /bin/ls, named __ls__. The symbolic link should be created in the current working directory.

## cp -n *.html ..

This command Create a script that copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.

## mv [[:upper:]]* /tmp/u

This is for Create a script that moves all files beginning with an uppercase letter to the directory /tmp/u.

## rm *~

This is for Create a script that deletes all files in the current working directory that end with the character ~.

## mkdir -p welcome/to/school

This Create a script that creates the directories welcome/, welcome/to/ and welcome/to/holberton in the current directory.

## ls -map

This is a command that lists all the files and directories of the current directory, separated by commas (,).

 - Directory names should end with a slash (/)
 - Files and directories starting with a dot (.) should be listed
 - The listing should be alpha ordered, except for the directories . and .. which should be listed at the very beginning
 - Only digits and letters are used to sort; Digits should come first
 - You can assume that all the files we will test with will have at least one letter or one digit
 - The listing should end with a new line
