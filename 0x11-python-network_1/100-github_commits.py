#!/usr/bin/python3
""" This script lists commits of a repository taking as
    arguments the username and owner name
"""
import requests
import sys


if len(sys.argv) == 3:
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = f"https://api.github.com/repos/{owner_name}/{repository_name}"
    response = requests.get(url)

    if response.status_code == 200:
        print(response.json())
    else:
        print("Error: {}".format(response.status_code))
