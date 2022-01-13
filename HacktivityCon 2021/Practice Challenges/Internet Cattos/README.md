# Internet Cattos | Warmups

*The internet is full of wonderful kittens and cattos!*

Connecting to the `nc` session:

```
$ nc challenge.ctf.games 31615
Oh, we already sent the flag! Did you see it?
```

I decided to output the hex dump to a file:

```
$ nc challenge.ctf.games 31615 -o dump
Oh, we already sent the flag! Did you see it?
```

The contents of this file are:

```
< 00000000 66 0d                                           # f.
< 00000002 6c 0d 61 0d 67 0d 7b 0d 74 0d 68 0d 69 0d 73 0d # l.a.g.{.t.h.i.s.
< 00000012 5f 0d 6e 0d 65 0d 74 0d 63 0d 61 0d 74 0d 5f 0d # _.n.e.t.c.a.t._.
< 00000022 73 0d 61 0d 79 0d 73 0d 5f 0d 6d 0d 65 0d 6f 0d # s.a.y.s._.m.e.o.
< 00000032 77 0d 7d 0d 4f 68 2c 20 77 65 20 61 6c 72 65 61 # w.}.Oh, we alrea
< 00000042 64 79 20 73 65 6e 74 20 74 68 65 20 66 6c 61 67 # dy sent the flag
< 00000052 21 20 44 69 64 20 79 6f 75 20 73 65 65 20 69 74 # ! Did you see it
< 00000062 3f 0a                                           # ?.
```

So, the flag is:

```
flag{this_netcat_says_meow}
```