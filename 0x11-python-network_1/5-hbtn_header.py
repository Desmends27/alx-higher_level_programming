#!/usr/bin/python3
"""Take a URL, send the request to the URL and display the value"""
import requests
from sys import argv

if __name__ == "__main__":
    r = requests.get(argv[1])
    print(r.headers.get('X-Request-Id'))
