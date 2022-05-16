#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        int(value)
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return False
