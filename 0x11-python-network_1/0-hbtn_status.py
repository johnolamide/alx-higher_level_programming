#!/usr/bin/python3
""" This script contains code to fetch from a URL
"""
from urllib.request import Request, urlopen


url = "https://alx-intranet.hbtn.io/status"
req = Request(url)

with urlopen(req) as response:
    data = response.read()
    print("Body response:")
    print("\t- type:", type(data))
    print("\t- content:", data)
    print("\t- utf8 content:", data.decode('utf-8'))
