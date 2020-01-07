#!/bin/bash
# Sends DELETE request to URL passed as first argument. Response then displayed.
curl -sX  DELETE "$@"
