# Kenobi Writeup

## Overview

This is my writeup for the Kenobi CTF.  The Kenobi CTF is a free room of easy difficulty which tests your ability to exploit Linux machines and enumerate Samba for shares.  This is an easy box which walks you through each step, so it is ideal for beginners who are new to penetration testing.

Also, as a side note, if the IP address is not consistent throughout this walkthrough, do not worry - I had a lot of problems with this box for some reason, so I had to restart it a bunch of times throughout the process.

## How to Access

I completed this CTF challenge on TryHackMe.

Link to the room:
- https://tryhackme.com/room/kenobi

## Steps

### Scanning and Enumeration

First, let's scan the machine for open ports using nmap:

```
$ sudo nmap -sC -sV -oN initial 10.10.105.153
# Nmap 7.91 scan initiated Thu May  6 16:50:13 2021 as: nmap -sC -sV -oN initial 10.10.105.153
Nmap scan report for 10.10.105.153
Host is up (0.093s latency).
Not shown: 993 closed ports
PORT     STATE SERVICE     VERSION
21/tcp   open  ftp         ProFTPD 1.3.5
22/tcp   open  ssh         OpenSSH 7.2p2 Ubuntu 4ubuntu2.7 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 b3:ad:83:41:49:e9:5d:16:8d:3b:0f:05:7b:e2:c0:ae (RSA)
|   256 f8:27:7d:64:29:97:e6:f8:65:54:65:22:f7:c8:1d:8a (ECDSA)
|_  256 5a:06:ed:eb:b6:56:7e:4c:01:dd:ea:bc:ba:fa:33:79 (ED25519)
80/tcp   open  http        Apache httpd 2.4.18 ((Ubuntu))
| http-robots.txt: 1 disallowed entry 
|_/admin.html
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Site doesn't have a title (text/html).
111/tcp  open  rpcbind     2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100003  2,3,4       2049/tcp   nfs
|   100003  2,3,4       2049/tcp6  nfs
|   100003  2,3,4       2049/udp   nfs
|   100003  2,3,4       2049/udp6  nfs
|   100005  1,2,3      35783/udp6  mountd
|   100005  1,2,3      52331/tcp   mountd
|   100005  1,2,3      54759/tcp6  mountd
|   100005  1,2,3      55177/udp   mountd
|   100021  1,3,4      34809/udp6  nlockmgr
|   100021  1,3,4      38109/tcp   nlockmgr
|   100021  1,3,4      41723/tcp6  nlockmgr
|   100021  1,3,4      60332/udp   nlockmgr
|   100227  2,3         2049/tcp   nfs_acl
|   100227  2,3         2049/tcp6  nfs_acl
|   100227  2,3         2049/udp   nfs_acl
|_  100227  2,3         2049/udp6  nfs_acl
139/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp  open  netbios-ssn Samba smbd 4.3.11-Ubuntu (workgroup: WORKGROUP)
2049/tcp open  nfs_acl     2-3 (RPC #100227)
Service Info: Host: KENOBI; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_clock-skew: mean: 1h39m59s, deviation: 2h53m12s, median: -1s
|_nbstat: NetBIOS name: KENOBI, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.3.11-Ubuntu)
|   Computer name: kenobi
|   NetBIOS computer name: KENOBI\x00
|   Domain name: \x00
|   FQDN: kenobi
|_  System time: 2021-05-06T10:50:26-05:00
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2021-05-06T15:50:26
|_  start_date: N/A

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Thu May  6 16:50:29 2021 -- 1 IP address (1 host up) scanned in 16.46 seconds
```

As we can see, there are **7** ports open on the machine.  Let's now run gobuster to see if we can fuzz for some directories:

```
$ gobuster dir -u http://10.10.105.153/ -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt 
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.105.153/
[+] Threads:        10
[+] Wordlist:       /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2020/04/07 11:43:04 Starting gobuster
===============================================================
/server-status (Status: 403)
===============================================================
2020/04/07 11:43:22 Finished
===============================================================
```

As shown, there are no directories which we can look at.  So let's keep enumerating until we find something.  I used the given SMB nmap scan command to check for any public SMB shares:

```
$ nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse 10.10.105.153
Starting Nmap 7.91 ( https://nmap.org ) at 2021-05-06 17:09 BST
Nmap scan report for 10.10.105.153
Host is up (0.030s latency).

PORT    STATE SERVICE
445/tcp open  microsoft-dsss

Host script results:
| smb-enum-shares: 
|   account_used: guest
|   \\10.10.225.226\IPC$: 
|     Type: STYPE_IPC_HIDDEN
|     Comment: IPC Service (kenobi server (Samba, Ubuntu))
|     Users: 2
|     Max Users: <unlimited>
|     Path: C:\tmp
|     Anonymous access: READ/WRITE
|     Current user access: READ/WRITE
|   \\10.10.225.226\anonymous: 
|     Type: STYPE_DISKTREE
|     Comment: 
|     Users: 0
|     Max Users: <unlimited>
|     Path: C:\home\kenobi\share
|     Anonymous access: READ/WRITE
|     Current user access: READ/WRITE
|   \\10.10.225.226\print$: 
|     Type: STYPE_DISKTREE
|     Comment: Printer Drivers
|     Users: 0
|     Max Users: <unlimited>
|     Path: C:\var\lib\samba\printers
|     Anonymous access: <none>
|_    Current user access: <none>

Nmap done: 1 IP address (1 host up) scanned in 5.11 seconds
```

So it looks like there are **3** shares on the machine.  In particular, we have an anonymous share which allows anonymous access.  Let's go ahead and access this using smbclient:

![smbclient](screenshots/2_smbclient.png)

As shown above, there is a **log.txt** file stored on the share.  We can retrieve this using smbget as shown below:

![smbget](screenshots/3_smbget.png)

Most of this log file is useless, but there are a few interesting pieces which we can use:

```
Generating public/private rsa key pair.
Enter file in which to save the key (/home/kenobi/.ssh/id_rsa): 
Created directory '/home/kenobi/.ssh'.
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/kenobi/.ssh/id_rsa.
Your public key has been saved in /home/kenobi/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:C17GWSl/v7KlUZrOwWxSyk+F7gYhVzsbfqkCIkr2d7Q kenobi@kenobi
The key's randomart image is:
+---[RSA 2048]----+
|                 |
|           ..    |
|        . o. .   |
|       ..=o +.   |
|      . So.o++o. |
|  o ...+oo.Bo*o  |
| o o ..o.o+.@oo  |
|  . . . E .O+= . |
|     . .   oBo.  |
+----[SHA256]-----+
```

This is information generated for the kenobi user when generating SSH keys.

```
# This is a basic ProFTPD configuration file (rename it to 
# 'proftpd.conf' for actual use.  It establishes a single server
# and a single anonymous login.  It assumes that you have a user/group
# "nobody" and "ftp" for normal operation and anon.

ServerName			"ProFTPD Default Installation"
ServerType			standalone
DefaultServer			on

# Port 21 is the standard FTP port.
Port				21
```

This machine is using ProFTPD which is an open-source FTP server for UNIX and Windows systems.  It is running this service on port **21**.

From our initial nmap scan, it shows that port 111 is running rpcbind.  This is simply a server which converts remote prodecure call (RPC) program number to universal addresses.  When an RPC service starts, it tells rpcbind the address it is listening on and the RPC program number it is prepared to serve.  

In this case, port 111 is used to access a network file system.  We can use nmap to enumerate this further using, as shown below:

![rpc enumerate](screenshots/4_rpc_enumerate.png)

It shows that ther is a **/var** mount on the system.

### Gaining Access

We will use ProFTPD to gain access into this machine.  But first, we need to know the version in order to check for vulnerabilities.  We can do this using netcat:

![proftpd enumerate](screenshots/5_proftpd_enumeration.png)

Now that we know that the machine is running version **1.3.5** of ProFTPD, we can use searchsploit to find potential vulnerabilities:

![searchsploit](screenshots/6_searchsploit.png)

It shows **3** exploits for this particular version of ProFTPD.  We shall be using the vulnerable `mod_copy` module.  This module implements two commands: `SITE CPFR` and `SITE CPTO`.  These commands allow you to copy files/directories from one place to another on a server.  Any unauthenticated user can leverage these commands to copy files from any part of the filesystem to a specified destination.

As shown from the log file, there is an SSH key generated for the kenobi user.  We can use FTP to download the private key to our system so that we can login as the kenobi user.

![exploiting](screenshots/7_exploiting.png)

As shown above, the kenobi user's private key has been moved to the `/var/tmp` directory - which we can access using rpc.  Now, let's mount the `/var/tmp` directory to our machine:

![mounting var](screenshots/8_mounting_var.png)

We now have a network mount on our machine.  Let's copy the private key to our current directory and use it to log in as kenobi:

![gaining access](screenshots/9_gaining_access.png)

Let's retrieve the first flag from the `/home/kenobi` directory:

![flag1](screenshots/10_flag1.png)

### Privilege Escalation

For this final part, we must escalate our privileges so that we can view the final flag in the `/root` directory.  Firstly, let's see if there are any strange binaries which we can run as kenobi:

![searching binaries](screenshots/11_searching_binaries.png)

To a beginner, this may seem hard to try and pick anything out of the ordinary.  Unfortunately, this is the only part of this CTF where prior experience comes in really handy.  However, if you want an easy way to check which binaries should have a set uid bit, run the command on your own system and compare the results with the target system.

In this case, the binary which stands out is the **`/usr/bin/menu`** binary.  Running this provides us with **3** options:

![running binary](screenshots/12_running_binary.png)

I also ran `strings` which is a Linux command that looks for human readable elements in a binary:

![strings](screenshots/13_strings.png)

This shows that the binary is running without the full path, i.e., `curl` should be `/usr/bin/curl` and `uname` should be `/usr/bin/uname`.  Since this binary is run with root privileges, we can manipulate our path to gain a root shell, as shown below:

![privilege escalation](screenshots/14_priv_esc.png)

Here, we copy the `/bin/sh` shell and call it "curl".  We then give it the correct permissions and put its location in our PATH.  This means that when `/usr/bin/menu` is executed, it is executed using our PATH variable to find the "curl" binary, which is actually a version of `/usr/sh`.  So, as well as running this binary as root, it also runs our shell as root.  This means we can view our final flag:

![flag2](screenshots/15_flag2.png)

And that's it!

## Summary and Feedback

