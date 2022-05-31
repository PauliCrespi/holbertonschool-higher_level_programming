#!/usr/bin/python3
"""task 8"""
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
"""import func"""
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
"""import func"""


filename = "add_item.json"
list = []
try:
    list = load_from_json_file(filename)
except FileNotFoundError:
    lista = []

list.extend(argv[1:])
save_to_json_file(list, "add_item.json")
