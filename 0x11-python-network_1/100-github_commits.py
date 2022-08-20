#!/usr/bin/python3
"""task 100"""

from sys import argv
from requests import get


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    req = get(url)
    for commit in req.json()[0:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
