#!/bin/bash
#task 101
curl -sH "Content-Type: application/json" -d @"$2" "$1"
