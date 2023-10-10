#!/usr/bin/python3
""" The module: 7-add_item"""


from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file



obj1 = argv[1:]

save_to_json_file(obj1, "add_item.json")
load_from_json_file("add_item.json")
