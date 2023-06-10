#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """replace an element in a list at a specific position
      without modifying the original list

    Args:
        my_list: list variable
        idx: index
        element: value

    Returns:
        Updated list
    """
    if (idx < 0):
        return my_list
    elif (idx >= len(my_list)):
        return my_list
    else:
        new_list = my_list[:]
        new_list[idx] = element
    return new_list


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    idx = 3
    new_element = 9
    new_list = new_in_list(my_list, idx, new_element)

    print(new_list)
    print(my_list)
