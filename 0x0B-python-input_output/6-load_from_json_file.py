#!/usr/bin/python3
"""task 6"""
import json


def load_from_json_file(filename):
    """Write a function that creates an Object from a son"""
    with open(filename, 'r', encoding="utf-8") as f:
        json_object = json.load(f)
    return(json_object)
    return(type(json_object))
