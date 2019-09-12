# SHELL PERMISSIONS

## 0-iam_betty

This script is for changes your user ID to betty.

## 1-who_am_i

This script is for prints the effective userid of the current user.

## 2-groups

This script is for prints all the groups the current user is part of.

## 3-new_owner

This script is for changes the owner of the file hello to the user betty.

## 4-empty

This script is for creates an empty file called hello.

## 5-execute

This script is for adds execute permission to the owner of the file hello.

## 6-multiple_permissions

This script is for adds execute permission to the owner and the group owner, and read permission to other users, to the file hello.

## 7-everybody

This script is for adds execution permission to the owner, the group owner and the other users, to the file hello.

## 8-James_Bond

This script is for sets the permission to the file hello as follows:

- Owner: no permission at all.
- Group: no permission at all.
- Other users: all the permissions.

## 9-John_Doe

This script is for sets the mode of the file hello to this:

-rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello

- The file hello will be in the working directory.
- You are not allowed to use commas for this script.

## 10-mirror_permissions

This script is for sets the mode of the file hello the same as ollehs mode.

- The file hello will be in the working directory.
- The file olleh will be in the working directory.

## 11-directories_permissions

This script is for adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users. Regular files should not be changed.

## 12-directory_permissions

This script is for creates a directory called dir_holberton with permissions 751 in the working directory.

## 13-change_group

This script is for changes the group owner to holberton for the file hello.

- The file hello will be in the working directory.

## 14-change_owner_and_group

This script is for changes the owner to betty and the group owner to holberton for all the files and directories in the working directory.

## 15-symbolic_link_permissions

This script is for changes the owner and the group owner of the file _hello to betty and holberton respectively.

- The file _hello is in the working directory.
- The file _hello is a symbolic link.

## 16-if_only

This script is for changes the owner of the file hello to betty only if it is owned by the user guillaume.

- The file hello will be in the working directory.
