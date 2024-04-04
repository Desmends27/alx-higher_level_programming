#!/usr/bin/python3
"""Takes in a url and send an email address to the passed URL"""
import requests
from sys import argv

if __name__ == "__main__":
    r = requests.post(argv[1], data={"email": argv[2]})
    print(r.text)
