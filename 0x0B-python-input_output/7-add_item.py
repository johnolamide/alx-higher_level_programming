#!/usr/bin/python3
""" Module contains the function definition for add_item
"""
import sys
import json
from os import path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


args = sys.agv[1:]
filename = "add_item.json"

if path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

my_list.extend(args)
save_to_json_file(my_list, filename)
