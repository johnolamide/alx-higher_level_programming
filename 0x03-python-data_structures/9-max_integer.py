#!/usr/bin/python3
def max_integer(my_list=[]):
    """Finds the biggest integer in a list

    Args:
        my_list: list of integers

    Returns:
        max of the integers
    """
    if not my_list:
        return None
    max_int = my_list[0]
    for i in my_list:
        if i > max_int:
            max_int = i
    return max_int


if __name__ == "__main__":
    my_list = [1, 90, 2, 13, 34, 5, -13, 3]
    max_value = max_integer(my_list)
    print("Max: {}".format(max_value))
