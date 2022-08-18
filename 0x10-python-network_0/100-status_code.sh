#!/bin/bash
#task 100
curl -so /dev/null -I -w "%{http_code}"  "$1"
