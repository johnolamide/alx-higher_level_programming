#!/usr/bin/python3
""" This script takes a letter and sends a POST request
"""
import requests
import sys


if len(sys.argv) > 1:
    q = sys.argv[1]
else:
    q = ""

url = 'http://0.0.0.0:5000/search_user'
data = {'q': q}
response = requests.post(url, data)

try:
    json_response = response.json()
    if json_response:
        id = json_response.get('id')
        name = json_response.get('name')
        print("[{}] {}".format(id, name))
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")
