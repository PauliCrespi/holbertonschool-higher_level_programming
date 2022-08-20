#!/usr/bin/python3
"""task 2"""
import urllib.parse
import urllib.request
from sys import argv


if __name__ == "__main__":
    mail = {'email': argv[2]}
    parenc = urllib.parse.urlencode(mail).encode()
    req = urllib.request.Request(argv[1], parenc)
    with urllib.request.urlopen(req) as response:
        html = response.read()
    print(html.decode("utf-8"))
