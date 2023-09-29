#!/usr/bin/python3
""" This script takes in an URL sends a request and displays
    the variable X-Request-Id
"""
import requests
import sys


if len(sys.argv) == 2:
    url = sys.argv[1]
    response = requests.get(url)

    print(response.headers.get('X-Request-Id'))
