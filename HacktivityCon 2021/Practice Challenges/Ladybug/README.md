# Ladybug | Web

*Want to check out the new Ladybug Cartoon? It's still in production, so feel free to send in suggestions!*

Visiting the link, we are greeted with a seemingly normal landing page.

A quick inspection of the source code shows the paths for the images: `/film/<file>`.  Trying to go to a random non-existing page, takes us to an errored page showing a Python terminal error.  Setting `debug=True`, we are able to see the full debug output.  As part of this console, if `debug` is enabled, we can get a Python terminal open.

Using the Python debugging console, we are able to execute arbitrary Python commands and thus can enumerate the flag location and printing out:

```
[console ready]
>>> import os
>>> os.listdir()
['flag.txt', 'templates', 'main.py', 'requirements.txt']
>>> print(open('flag.txt','r').read())
flag{weurkzerk_the_worst_kind_of_debug}
```