#!/usr/bin/python3
""" Takes a letter and sends a post request with the letter as param """
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) == 2:
        q = {"q": argv[1]}
    else:
        q = {}
    r = requests.post('http://0.0.0.0:5000/search_user', data=q)
    try:
        response_data = r.json()
        if 'id' in response_data and 'name' in response_data:
            print("[{}] {}".format(response_data['id'], response_data['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
