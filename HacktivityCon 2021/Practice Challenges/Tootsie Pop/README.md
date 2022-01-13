# Tootsie Pop | Scripting

*How may licks does it take to get to the center of a tootsie pop?*

In `bash`, in an empty directory, place the `pop.zip` file and execute the following:

```bash
while true; do find . -type f | while read f; do mv "$f" "1";7z -y e "1"; done; done
```

The flag is:

```
flag{the_answer_is_1548_licks}
```