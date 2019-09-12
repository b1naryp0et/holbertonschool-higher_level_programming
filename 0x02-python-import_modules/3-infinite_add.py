#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    x = 0
    for y in range (1, len(argv)):
        x = x + int(argv[y])
    print(x)
