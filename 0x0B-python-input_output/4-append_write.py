#!/usr/bin/python3


def append_write(filename="", text=""):
    with open(filename, 'at') as f:
        return f.write(text)
