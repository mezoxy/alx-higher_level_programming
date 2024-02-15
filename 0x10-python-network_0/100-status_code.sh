#!/bin/bash
# A Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response.

curl -o header.txt -sI "$1" 
awk '/^HTT/{print $2}' header.txt
