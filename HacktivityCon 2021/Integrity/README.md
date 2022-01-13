# Integrity | Web (container)

*My school was trying to teach people about the CIA triad so they made all these dumb example applications... as if they know anything about information security.*

*Supposedly they learned their lession and tried to make this one more secure. Can you prove it is still vulnerable?*

With this newly updated site, some characters are not allowed.

Looking at potential [bypasses](https://book.hacktricks.xyz/pentesting-web/command-injection), I was able to pass `ls %0A cat flag.txt` to get the flag:

```
flag{62b8b3cb5b8c6803bf3dc585b1b5141d}
```