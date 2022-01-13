# Buffer Overflow | Warmups (container)

*Can you overflow this right?*

```
$ file butter_overflow                       
butter_overflow: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=f9d42ef66d8218f0514030a2fae48b91206f9a34, for GNU/Linux 3.2.0, not stripped
```

```
$ checksec --file butter_overflow 
[*] Checking for new versions of pwntools
    To disable this functionality, set the contents of /home/v3r4x/.cache/.pwntools-cache-3.9/update to 'never' (old way).
    Or add the following lines to ~/.pwn.conf or ~/.config/pwn.conf (or /etc/pwn.conf system-wide):
        [update]
        interval=never
[*] You have the latest version of Pwntools (4.6.0)
[*] '/home/v3r4x/ctfs/hacktivitycon/butter_overflow/task/butter_overflow'
    Arch:     amd64-64-little
    RELRO:    Full RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      PIE enabled

```


```
int main() {
    char buffer[0x200];

    setbuf(stdout, NULL);
    setbuf(stdin, NULL);

    signal(SIGSEGV, handler);

    puts("How many bytes does it take to overflow this buffer?");
    gets(buffer);

    return 0;
}
```

- reads in 512 in bytes for `buffer`
- `signal` handles segmentation faults and calls `handler()` which calls `give_flag()`

Program crashes after 520 bytes

Connecting to the server and pasting in the string gets the flag:

```
flag{72d8784a5da3a8f56d2106c12dbab989}
```