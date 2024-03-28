#!/bin/bash
#send a url to a server and displays the size
sudo curl -w "%{size_download}\n" -o /dev/null -s "$1"
