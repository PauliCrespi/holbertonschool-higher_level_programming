#!/usr/bin/python3
"""task 6"""
import requests
import sys


req = requests.post(sys.argv[1], data={'email': sys.argv[2]})
print(req.text)
