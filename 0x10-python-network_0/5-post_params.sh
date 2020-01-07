#!/bin/bash
# Takes in URL, sends POST request to passed URL, and displays response
curl -sd "email=hr@holbertonschool.com" -d "subject=I will always be here for PLD" "$@"
