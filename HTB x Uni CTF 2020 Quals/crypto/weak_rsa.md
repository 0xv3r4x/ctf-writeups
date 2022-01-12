# Weak RSA

This was the first challenge I completed and was probably the easiest to do.  You were given a public key file: pubkey.pub and an encrypted file containing the flag: flag.enc.

I first extracted the modulus and the exponent from the public key file using openssl:

```
$ openssl rsa -pubin -in pubkey.pub -text -noout
RSA Public-Key: (1026 bit)
Modulus:
    03:64:a5:37:f4:1c:bb:40:a1:ce:a1:d7:93:5a:f4:
    ae:25:e6:68:b9:c7:bf:3d:79:3c:d0:bc:66:55:8d:
    85:61:03:5b:46:73:9a:de:4a:c6:cd:0f:fc:ac:90:
    e2:ac:40:3d:b5:77:c2:ef:74:14:f0:10:5c:be:fc:
    29:dd:db:c8:69:bc:de:1a:37:3e:e8:58:3b:d8:6c:
    b6:cc:a6:96:fc:72:0c:fd:96:b4:7d:51:f6:c9:35:
    14:81:c8:fe:b7:12:78:d0:b2:6f:ab:87:c5:55:70:
    28:68:a6:88:53:7d:7a:e6:42:40:9d:e6:19:a7:ca:
    d3:e8:e4:47:24:90:8a:bc:df
Exponent:
    02:28:48:1c:f1:27:03:1c:41:4c:44:58:cf:05:1d:
    ad:dd:d6:1b:74:ab:0e:4b:b7:c7:32:49:85:48:ec:
    09:a2:9e:96:6e:55:6d:a8:29:53:df:0a:cc:68:02:
    fb:47:03:c1:02:af:52:58:91:fa:2e:9b:e2:9f:81:
    05:2a:d0:45:cb:b6:d7:74:bb:37:4f:cf:67:1d:e7:
    80:83:ad:da:5a:5b:3b:a4:77:23:69:d5:62:ed:cd:
    ad:4c:3e:01:6e:33:9b:26:3b:84:70:a2:07:d9:9e:
    53:7b:b1:a2:4e:57:8a:cf:29:dc:64:ff:f0:c0:08:
    0d:9f:64:c8:e7:ee:bf:51:89
```

As you can see both the modulus and the exponent are in hexadecimal format.  Since the number outputted by both conversions are really big, I'll use placeholders from now on.

So now it's just a question of finding the flag.  After a quick Google search, I found a GitHub repo specifically made for RSA CTF challenges - no harm in trying this then.

https://github.com/Headorteil/RsaCtfTool

Using both decimal values for the modulus and exponent, I ran the following command

```
$ python3 RsaCtfTool.py -n [modulus] -e [exponent] --uncipherfile flag.enc
[+] Clear text : b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00HTB{b16_e_5m4ll_d_3qu4l5_w31n3r_4774ck}'
```

The last part is our flag! 

flag: ```HTB{b16_e_5m4ll_d_3qu4l5_w31n3r_4774ck}```
