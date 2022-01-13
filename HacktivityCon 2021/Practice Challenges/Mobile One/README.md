# Mobile One

*The one true mobile app*

Running the following against the `.apk` gets the flag:

```
strings mobile_one.apk | grep "flag{" | cut -d "#" -f 3 > flag.txt
```

```
flag{strings_grep_and_more_strings}
```