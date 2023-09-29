#!/usr/bin/python3
""" This script lists commits of a repository taking as
    arguments the username and owner name
"""
import requests
import sys


def list_commits(repository_name, owner_name):
    url = f"""
        https://api.github.com/repos/
        {owner_name}/{repository_name}/commits?per_page=10"""

    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()
        for commit in commits:
            sha = commit["sha"]
            author_name = commit["commit"]["author"]["name"]
            print(f"{sha}: {author_name}")
    else:
        message = f"""
            Error: Unable to fetch commits
             (HTTP Status Code {response.status_code})"""


if __name__ == "__main__":
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]

    list_commits(repository_name, owner_name)
