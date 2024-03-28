#!/bin/bash
#takes a url and displays the http methods the server will accept
curl -i  -X OPTIONS -s "$1" | grep "Allow: " | cut -d' ' -f2-
