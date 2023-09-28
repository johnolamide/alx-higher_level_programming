#!/bin/bash
# sends a POST request to the URL
curl -s -X POST -d "email=test@gmail.com&subject=I%20will%always%20be%20here%20for%20PLD" "$1"
