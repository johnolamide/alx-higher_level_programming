#!/usr/bin/python3
""" This script takes in a URL, sends a request and displays the
    response body
"""
from urllib.request import Request, urlopen
from urllib.error import HTTPError
import sys


if len(sys.argv) == 2:
    url = sys.argv[1]
    try:
        with urlopen(url) as response:
            data = response.read()
            print(data.decode('utf-8'))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
