#!/usr/bin/python3
""" This script takes in a URL and returns the value of X-Request-Id
"""
from urllib.request import Request, urlopen
import sys


if len(sys.argv) == 2:
    url = sys.argv[1]
    with urlopen(url) as response:
        info = response.info()
        print(info['X-Request-Id'])
