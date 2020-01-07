#!/bin/bash
# Script which takes in URL and displays all HTTP methods server will accept.
curl -sI "$@" | grep "Allow" | cut -d ' ' -f2-
