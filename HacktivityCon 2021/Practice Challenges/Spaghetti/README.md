# Spaghetti | Warmups

*It's a classic, it's everyones favorite, it's spaghetti! The long noodles are the best!*

Since the "long" noodles, I ran strings with `-e l`

```
$ strings -e l spaghetti.png
flag{wow_that_was_a_long_string_of_spaghetti}
```

Can also use `binwalk`:

```
$ binwalk -e spaghetti.png

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 520 x 300, 8-bit/color RGBA, non-interlaced
59            0x3B            Zlib compressed data, best compression

```

It appears that a Zlib file is hidden underneath.  Can use [FILExt](https://filext.com/file-extension/ZLIB) to view this extracted information from `_spaghetti.png.extracted/3B.zlib`:

```
 BIIIIIII) JJJJJJJJ  PRRRRRRR
 BIIIIIII) JJJJJJJJ  PRRRRRRR
 BIIIIIII) JJJJJJJ
À x2wP?9f83*~
Œ¯ o3xb e2 v>^F82V
 _O`vQ ^yFLsp
× 6o*vn5Lv=u
 tEXtSoftware Adobe ImageReadyq
 flag{wow_that_was_a_long_string_of_spaghetti}
```