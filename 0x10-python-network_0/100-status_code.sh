#!/bin/bash
# A Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response.
awk '/^HTT/{printf $2}' <(curl -sI "$1")
