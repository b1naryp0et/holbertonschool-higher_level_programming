#!/bin/bash
# Script which sends DELETE request to URL passed as first argument and displays body of response
curl -sX DELETE "$@"
