# Tyrannosaurus Rex | Cryptography

*We found this fossil. Can you reverse time and bring this back to life?*

For this challenge, you are given a Python file with an encrypted file in variable `c` and the function that was used to encrypt it `enc()`.

Looking at the `enc` function:

```python
def enc(f):
    e = b(f)
    z = []
    i = 0
    while i < len(e):
        z += [ e[i] ^ e[((i + 1) % len(e))]]
        i = i + 1
    c = h(bytearray(z))
    return c
```

Firstly, the flag (plaintext) is converted to Base 64 using `base64.b64encode()`, which is stored in variable `e`.  Then, each two consecutive characters in `e` is XORed to form a list of integers stored in `z`.  The last letter is XORed with the first one, which is indicated by `% len(e)`.  Finally, `z` is converted to hex using `binascii.hexlify()`.

Since we know the flag format, i.e., starts with `flag{`, we can run `base64.b64encode(b"flag")` to see how that would look in Base 64.  We get `b"ZmxhZw==`.  The first character `Z` has a decimal value of `90`.  We can use this in our decryption function:

First, I rewrote the `enc()` function to improve readiblity:

```python
def encrypt(plaintext):
    """
     Encryption function works as follows:

     1) Encode plaintext to Base 64
     2) XOR every two consecutive letters (last with first, etc.)
     3) Encode into hex
    """
    # encode plaintext in base 64
    encoded = base64.b64encode(plaintext)

    xor = []
    i = 0

    # XOR every two consecutive letters
    # last letter XORed with the first (% len(e))
    while i < len(encoded):
        xor += [encoded[i] ^ encoded[((i + 1) % len(encoded))]]
        i += 1

    # encode the ciphertext into hex
    ciphertext = binascii.hexlify(bytearray(xor))
    return ciphertext
```

To write this `decrypt()` function, we first need to reverse the encryption process and decrypt `z` or `xor` from right to left.  Since the last integer in this is the XOR of the last and first character in the Base 64 representation of the flag, we can XOR `90` with the last character of `xor` to get the last character of the flag.  This works because the XOR operation has the following property `A ^ A = 0`, therefore `A ^ A ^ B = B`.  Using the last character of the flag, we can get the second-last, and so on:

```python
def decrypt(ciphertext):
    """
     Decryption function works as follows:

     1) Decode ciphertext from hex and place into list format
     2) Reverse XOR from right to left
     3) Decode encoded text from Base 64 to give plaintext
    """
    # decode from hex and put into list format
    xor = list(binascii.unhexlify(ciphertext))

    i = len(xor) - 1
    encoded = b""
    last = 90  # base64.b64encode(b"flag")[0]

    while i >= 0:
        last ^= xor[i]
        encoded = chr(last).encode("utf-8") + encoded
        i -= 1

    plaintext = base64.b64decode(encoded)
    return plaintext
```

Running this function with the ciphertext `c`, we get the flag:

```
$ python3 fossil.py
b'flag{tyrannosauras_xor_in_reverse}'
```
