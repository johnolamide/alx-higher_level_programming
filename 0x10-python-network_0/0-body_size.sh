#!/bin/bash
# this script sends a request and returns the size of the body
curl -s "$1" | wc -c
