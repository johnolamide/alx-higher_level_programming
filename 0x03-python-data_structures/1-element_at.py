#!/usr/bin/python3
def element_at(my_list, idx):
    """retrieves the element at an index

    Args:
        my_list: list variable
        idx: index

    Returns:
        The element at the index
    """
    if (idx < 0):
        return None
    elif (idx >= len(my_list)):
        return None
    else:
        element = my_list[idx]
        return element


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    idx = 3
    print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
