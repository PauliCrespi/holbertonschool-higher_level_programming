#!/usr/bin/python3
"""task 3"""
import urllib.error
import urllib.request
from sys import argv


if __name__ == "__main__":
    req = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(req) as r:
            html = r.read()
    except urllib.error.HTTPError as e:
        print("Error code: " + err.code)
    else:
        print(html.decode("utf-8"))
