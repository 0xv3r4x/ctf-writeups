# Bits | Web

*Want to learn about binary units of information? Check out the "Bite of Knowledge" website!*

Not much information on the home page.  Manually crawling through the links reveals that all links are tied to `http://j2hi.com:50010/?page={page}`

The most logical guess is `http://j2hi.com:50010/?page=flag`.  This contains the text:

```
The flag is at /flag.txt
```

This could be Local File Inclusion (LFI).  Going to `http://j2hi.com:50010/?page=/../../../../../flag.txt` gave the text:

```
Sorry, /../../../../../flag.txt does not exist.
```

This means that the server is reading the page as `/../../../../../flag.txt.php` instead of just `/../../../../../flag.txt`.

However, if we include a null byte (`%00`), we can confuse the server to execute the code (`http://j2hi.com:50010/?page=/../../../../../flag.txt%00`).  This causes a break in the `.php` so the extension isn't included at the end fo the file.  The flag is:

```
flag{life_just_needed_a_null_byte}
```