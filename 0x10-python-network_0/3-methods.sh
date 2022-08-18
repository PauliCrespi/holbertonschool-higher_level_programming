#!/bin/bash
#task 3
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d" " -f 2- 
