#!/usr/bin/python3
"""task 9"""


class Student:
    """class student"""
    def __init__(self, first_name, last_name, age):
        """init"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """to json func"""
        if type(attrs) == list:
            for element in attrs:
                if type(element) != str:
                    break
            new = {}
            for i in attrs:
                if i in self.__dict__:
                    new[i] = self.__dict__[i]
            return(new)
        return (self.__dict__)

    def reload_from_json(self, json):
        """reload_from_json"""
        for key, value in json.items():
            setattr(self, key, value)
