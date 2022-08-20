#!/usr/bin/python3
"""task 4"""
from sys import argv
import requests


req = requests.get('https://intranet.hbtn.io/status')
print("Body response:")
print("\t- type: {}".format(type(req.text)))
print("\t- content: {}".format(req.text))
