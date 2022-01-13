# Common Place | Warmups

*asd7138: can you find the flag here?
tcm3137: no, i dont see it
jwh8163: i cant find it either
rfc5785: i found it
asd7138: what!? where?!
jwh8163: tell us!*

It appears `rfc5785` found the flag.  The RFC5785 document contains the following:

```
Abstract

   This memo defines a path prefix for "well-known locations",
   "/.well-known/", in selected Uniform Resource Identifier (URI)
   schemes.
```

Checking `/.well-known`, reveals a `flag.txt` file containing:

```
flag{rfc5785_defines_yet_another_common_place}
```