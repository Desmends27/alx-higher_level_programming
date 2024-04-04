#!/usr/bin/python3
""" Takes in url, sends a request to the url and displays the body """
import requests
from sys import argv

if __name__ == "__main__":
    r = requests.get(argv[1])
    if r.ok:
        print(r.text)
    else:
        print("Error code: {}".format(r.status_code))
