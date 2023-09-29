#!/usr/bin/python3
""" This script takes in a URL, sends a request to the URL
    and displays the body of the response
"""
import requests
import sys


if len(sys.argv) == 2:
    url = sys.argv[1]
    response = requests.get(url)

    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
