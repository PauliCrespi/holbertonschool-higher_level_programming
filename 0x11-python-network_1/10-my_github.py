#!/usr/bin/python3
"""task 10"""
import requests
from sys import argv

if __name__ == "__main__":
    data = (argv[1], argv[2])
    req = requests.get('https://api.github.com/user', auth=data)
    print(req.json().get('id'))
