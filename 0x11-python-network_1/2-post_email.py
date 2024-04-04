#!/usr/bin/python3
"""Takes i a URL and an email and send a post request to the url"""

from urllib import parse, request
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    values = {'email': argv[2]}
    data = parse.urlencode(values)
    data = data.encode('ascii')

    req = request.Request(url, data, method='POST')

    with request.urlopen(req) as response:
        the_page = response.read()
        print(the_page.decode('UTF-8'))
