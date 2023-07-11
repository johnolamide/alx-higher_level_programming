#!/usr/bin/python3
""" Module contains the function definition of read_file
"""


def read_file(filename=""):
    """ Reads a file and prints to stdout
        Args:
            filename: name of the file
    """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end='')


if __name__ == "__main__":
    read_file("my_file_0.txt")
