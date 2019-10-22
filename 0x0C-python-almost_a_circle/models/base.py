#!/usr/bin/python3
"""Module for Base """

import json
import os.path
import io


class Base:
    """The class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON dictionary"""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save JSON string to file"""

        if list_objs is None:
            list_objs = []
        list_objs = [comps.to_dictionary() for comps in list_objs]
        list_objs = cls.to_json_string(list_objs)
        with open(cls.__name__ + '.json', 'w') as file:
            file.write(list_objs)

    @staticmethod
    def from_json_string(json_string):
        """Format string as format"""

        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Dictionary Return"""

        if cls.__name__ == 'Rectangle':
            hbr = cls(1, 1)
        if cls.__name__ == 'Square':
            hbr = cls(1)
        hbr.update(**dictionary)
        return hbr

    @classmethod
    def load_from_file(cls):
        """Load a list of instances from a JSON file"""

        if not os.path.exists(cls.__name__ + '.json'):
            return []
        with open(cls.__name__ + '.json', 'r') as file:
            ide = cls.from_json_string(file.read())
        return [cls.create(**api) for api in ide]
