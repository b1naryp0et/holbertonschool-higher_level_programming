#!/bin/bash
# Takes in URL as argument, sends GET request to URL, and displays response
curl -s "$@" -H "X-HolbertonSchool-User-Id: 98"
