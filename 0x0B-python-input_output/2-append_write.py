#!/usr/bin/python3
""" Module contains the function definition of append_write
"""


def append_write(filename="", text=""):
    """ Appends a string at the end of a text file
        Args:
            filename: name of the file
            text(str): text string

        Returns:
            the number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)


if __name__ == "__main__":
    nb_characters_added = append_write("file_append.txt",
                                       "This School is so cool!\n")
    print(nb_characters_added)
