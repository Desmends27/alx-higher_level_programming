#!/bin/bash
#takes a url and sends a post request to the url
curl -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" -s "$1"
