#!/usr/bin/python3
"""Class Base"""
import json


class Base:
    """class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """inisialization"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """to json func"""
        if list_dictionaries is None:
            return []
        if len(list_dictionaries) == 0:
            return []
        return (json.dumps(list_dictionaries))
