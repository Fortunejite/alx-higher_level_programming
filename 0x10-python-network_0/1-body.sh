#!/bin/bash
# Send GET request to the URL using curl
response=$(curl -s -o /dev/null -w "%{http_code}" "$1")
if [ "$response" -eq "200" ]
then
  curl -s "$1"
