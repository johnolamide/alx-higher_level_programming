#!/usr/bin/python3
""" Module contains function definition for write_file
"""


def write_file(filename="", text=""):
    """ Writes a string to a text file
        Args:
            filename: name of file
            text(str): string of text

        Returns:
            number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)


if __name__ == "__main__":
    nb_characters = write_file("my_first_file.txt",
                               "This School is so cool!\n")
    print(nb_characters)
