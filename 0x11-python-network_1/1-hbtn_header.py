#!/usr/bin/python3
"""Takes in a URL and send a request to the URL to display a value"""
from urllib import request
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    with request.urlopen(argv[1]) as response:
        value = response.headers.get('X-Request-Id')
        print(value)
