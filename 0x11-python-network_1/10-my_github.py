#!/usr/bin/python3
"""Authicates git credientials using the github api"""
import requests
from sys import argv
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":

    url = "https://api.github.com/user"
    auth = HTTPBasicAuth(argv[1], argv[2])
    response = requests.get(url, auth=auth)
    res_dict = response.json()
    print(res_dict.get('id'))
