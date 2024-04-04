#!/usr/bin/python3
"""Fetch  from an alx website """
from urllib import request

if __name__ == "__main__":
    with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        var = response.read()
        print("Body response:")
        print("\t- type: {}".format(var.__class__))
        print("\t- content: {}".format(var))
        print("\t- utf8 content: {}".format(var.decode("UTF-8")))
