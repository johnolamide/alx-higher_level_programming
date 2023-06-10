#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """print an integer list in reverse

    Args:
        my_list: integer list variable

    Returns:
        Prints the reversed list
    """
    for i in range(len(my_list)):
        idx = -(i + 1)
        print("{:d}".format(my_list[idx]))


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    print_reversed_list_integer(my_list)
