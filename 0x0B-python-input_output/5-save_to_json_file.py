#!/usr/bin/python3
"""function"""
import json


def save_to_json_file(my_obj, filename):
    """json"""
    with open(filename, 'w', encoding="utf-8") as f:
        write_data = f.write(json.dumps(my_obj))
