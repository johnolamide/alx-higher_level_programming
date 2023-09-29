#!/usr/bin/python3
""" This script takes URL and an email address and sends a POST request
"""
import requests
import sys


if len(sys.argv) == 3:
    url = sys.argv[1]
    email = sys.argv[2]

    payload = {'email': email}
    response = requests.post(url, data=payload)
    print(response.text)
