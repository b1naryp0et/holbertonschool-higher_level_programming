#!/bin/bash
# Sends JSON POST request to URL passed as first argument, and displays response
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
