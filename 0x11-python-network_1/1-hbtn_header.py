#!/usr/bin/python3
import urllib.request
from sys import argv


if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as response:
        html = urllib.read()
        print(response.headers.get('X-Request-Id'))
