#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """delete an item at a specific position on a list

    Args:
        my_list: list of integers
        idx: index

    Returns:
        modified list
    """
    if not my_list:
        return None
    if (idx >= len(my_list)):
        return my_list
    del my_list[idx]
    return my_list


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    idx = 3
    new_list = delete_at(my_list, idx)
    print(new_list)
    print(my_list)
