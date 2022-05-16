#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return(fct(*args))
    except (TypeError, ValueError, IndexError, ZeroDivisionError) as errors:
        print("Exception: {}".format(errors), file=sys.stderr)
        return None
