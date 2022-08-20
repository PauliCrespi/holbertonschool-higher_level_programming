#!/usr/bin/python3
"""task 7"""
import requests
from sys import argv

if __name__ == "__main__":
    req = requests.get(argv[1])
    if (req.status_code >= 400):
        print("Error code: " + str(req.status_code))
    else:
        print(req.text)
