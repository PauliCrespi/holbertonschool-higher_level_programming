#!/usr/bin/python3
"""task 6"""
import requests
from sys import argv

if __name__ == "__main__":
    req = requests.post(argv[1], data={'email': argv[2]})
    print(req.text)
