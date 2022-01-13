# Template Shack | Web

*Check out the coolest web templates online!*

The main page appears to be an online shop for web templates.  However, the site appears to be static with a note in the source code:

```
<!-- TODO: Finish developing the admin section and add functionality to manage the templates --\>
```

Inspecting the cookies reveals a `token` cookie with a value that looks like a JWT token.  Using `jwt.io` to decode the token, I found the following:

```
header:
{
	"typ": "JWT",
	"alg": "HS256"
}

body:
{
	"username": "guest"
}
```

A user is issued with a token from an authorative source (usually the server) who stamps the token with a cryptographic signature.  The user can now bring this signed token and show it as proof of who they are.  Whenever the server requires any form of user authentication, the user will pass the JWT token in the `Authorize` header.  If the signature is valid, the server will accept the user's token and allow the user to proceed to the area they are trying to access.  This is very useful for scaling web applications as the server does not have to maintain sessions for each user, however, giving the user control of the token can be a security risk if it is not configured properly.

One way of testing this configuration is to create your own token with the algorithm set to `none` and removing the signature.  In the past, many libraries would accept an unsigned token in this way, however, this did not work in this case.

Since the algorithm is `HS256`, it may be using a weak secret.  I ran a script to format the token in such a way that it could be understood by John the Ripper.  Then, I used this tool with the `rockyou.txt` wordlist to find the secret.  It returned almost instantly with the value: `supersecret`.

```
$ echo "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Imd1ZXN0In0.9SvIFMTsXt2gYNRF9I0ZhRhLQViY-MN7VaUutz9NA9Y" > for_john.hash
$ john for_john.hash -w=/usr/share/wordlists/rockyou.txt
$ john for_john.hash --show
?:supersecret
```

I then set the secret in `jwt.io` to craft the token.  I chose to try setting the username to `admin` first, then I updated the `token` cookie with the forged token and refresehed the page.  This gave me the admin page.

Clicking on the charts/tabels shows a custom 404 page.  This can often lead to (Server-Side Tempalte Injection) SSTI in Flask Web Applications (read more [here](https://www.onsecurity.io/blog/server-side-template-injection-with-jinja2/).  Sending `/admin/{{1+1}}` shows:

```
/admin/4
```

Now, sending `/admin/{{request.application.globals.builtins.import('os').popen('cat flag.txt').read()}}` payload, we are able to read the `flag.txt`:

```
flag{easy_jinja_SSI_RCE}
```