#!/usr/bin/python3
""" This script connects to you Github account using your
    username and password and displays your id
"""
import requests
import sys


if len(sys.argv) == 3:
    username = sys.argv[1]
    token = sys.argv[2]

    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(username, token))

    if response.status_code == 200:
        print(response.json().get('id'))
    else:
        print("Error: {}".format(response.status_code))
