#!/usr/bin/python3
"""task 5"""
import requests
import sys


if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    try:
        print(req.headers['X-Request-Id'])
    except KeyError:
        pass
