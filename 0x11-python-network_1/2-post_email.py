#!/usr/bin/python3
""" This Script takes a URL and email and sends a POST request
"""
from urllib.request import Request, urlopen
from urllib.parse import urlencode
import sys


if len(sys.argv) == 3:
    url = sys.argv[1]
    email = sys.argv[2]

    values = {'email': email}
    data = urlencode(values)
    data = data.encode('ascii')

    req = Request(url)
    with urlopen(req, data) as response:
        body = response.read()
        print(body.decode('utf-8'))
