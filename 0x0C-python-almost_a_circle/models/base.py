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

    @staticmethod
    def to_json_string(list_dictionaries):
        """to json func"""
        if list_dictionaries is None:
            return "[]"
        elif len(list_dictionaries) == 0:
            return "[]"
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """save json"""
        dic_lis = []
        if list_objs is None:
            list_objs = []
        for c in list_objs:
            dic_lis.append(c.to_dictionary())
        with open(cls.__name__ + '.json', 'w', encoding="utf-8") as f:
            f.write(cls.to_json_string(dic_lis))

    @staticmethod
    def from_json_string(json_string):
        """from json to string"""
        if json_string is None or len(json_string) == 0:
            return []
        return(json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """create func"""
        inst = cls(1, 1)
        if inst is not None:
            inst.update(**dictionary)
        return inst
