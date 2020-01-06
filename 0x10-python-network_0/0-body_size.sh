#!/bin/bash
# Script which takes in URL, sends request to that URL, and displays size of body of response

curl -s "$1" | wc -c
