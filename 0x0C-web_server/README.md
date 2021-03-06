# 0x0C. Web server

## Resources:books:

Read or watch:

* [How the web works](https://intranet.hbtn.io/rltoken/4tRRzyyETAySzU-bgNGLSw)
* [Nginx](https://intranet.hbtn.io/rltoken/H9OfhUnBDdxV-QQnIucMlA)
* [How to Configure Nginx](https://intranet.hbtn.io/rltoken/wePwmjbJDgJZO7YPvffWxQ)
* [Child process](https://intranet.hbtn.io/rltoken/V8RZRTiBQBweSGFenuQX5w)
* [Root and sub domain](https://intranet.hbtn.io/rltoken/d_7WpP7WEMKyPx6sG5VmlQ)
* [HTTP requests](https://intranet.hbtn.io/rltoken/C9s3U62JbiOAvn9WCoxKsA)
* [HTTP redirection](https://intranet.hbtn.io/rltoken/kI4vRQ6vc45Wfbdo3UD8Lw)
* [Not found HTTP response code](https://intranet.hbtn.io/rltoken/5UvC588x2hZR7dm6eRFPoQ)
* [Logs files on Linux](https://intranet.hbtn.io/rltoken/bkqQ72HZVAV65G8nB503Pw)

---

## Learning Objectives:bulb:

What you should learn from this project:

* What is the main role of a web server
* What is a child process
* Why web servers usually have a parent process and child processes
* What are the main HTTP requests

---

### [0. Transfer a file to your server](./0-transfer_file)

* Write a Bash script that transfers a file from our client to a server:

### [1. Install nginx web server](./1-install_nginx_web_server)

* 

### [2. Setup a domain name](./2-setup_a_domain_name)

* .TECH Domains is one of the top domain providers. They are known for the stability and quality of their DNS hosting solution. Holberton School partnered with .TECH Domains so that you can learn about DNS.

### [3. Redirection](./3-redirection)

* Configure your Nginx server so that /redirect_me is redirecting to another page.
* Requirements:
    * The redirection must be a “301 Moved Permanently”
    * You answer file should be a Bash script containing commands to automatically configure a Ubuntu machine to respect above requirements
    * Using what you did with 1-install_nginx_web_server, write 3-redirection so that it configures a brand new Ubuntu machine to the requirements asked in this task

### [4. Not found page 404](./4-not_found_page_404)

* Configure your Nginx server to have a custom 404 page that contains the string Ceci n'est pas une page.

---

## Author
**Joshua Martinez** - [dantsub](https://github.com/dantsub)
