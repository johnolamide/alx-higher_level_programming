#!/bin/bash
# this script displays body of 200 status code response
curl -s -w 200 "$1"
