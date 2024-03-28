#!/bin/bash
#Send a delete request to the url passed as the first argument
curl -X DELETE -Ls "$1"
