#!/usr/bin/python3
"""Sends a request to the URL and display the response body """
from urllib import request, error
from sys import argv

if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as response:
            var = response.read()
            print(var.decode("UTF-8"))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
