#!/bin/bash
#send a get request and set a variable
curl -GLs -H "X-School-User-Id:98" "$1"
