#!/usr/bin/python3

import json


def save_to_json_file(my_obj, filename):
    with open(filename, 'wt') as f:
        json.dump(my_obj, f)
