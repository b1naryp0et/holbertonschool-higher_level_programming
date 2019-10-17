#!/usr/bin/python3


def write_file(filename="", text=""):
    with open(filename, 'wt') as f:
        return f.write(text)
