#!/bin/bash
# this script displays body of 200 status code response
curl -s -w "%{http_code}" "$1" | awk 'NR==1 && $0==200 {getline; print}'
