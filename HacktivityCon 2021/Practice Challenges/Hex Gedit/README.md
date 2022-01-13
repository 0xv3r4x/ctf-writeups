# Hexgedit | Warmups

*Woah! Someone opened the flag file in hexedit... and then gedit??*

The file is an image of the hex output in `gedit`.  Since we know the flag format, we can search for `flag{` up to `}` in hex format - `66 6c 61 67 7b` to `7d`:

```
66 6c 61 67 7b 6f 70 74 69 63 61 6c 5f 68 65 78 61 64 65 63 69 6d 61 6c 5f 72 65 63 6f 67 6e 69 74 69 6f 6e 5f 61 6d 69 72 69 74 65 7d 
```

Converting this from hex to text, we get the flag:

```
flag{optical_hexadecimal_recognition_amirite}
```