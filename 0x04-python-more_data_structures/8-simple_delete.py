#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """deletes a key in a dictionary

    Args:
        a_dictionary: dictionary variable
        key: key

    Returns:
        modified dictionary
    """
    if key in a_dictionary:
        del a_dictionary[key]


if __name__ == "__main__":
    a_dictionary = {'language': "C", 'Number': 89,
                    'track': "Low", 'ids': [1, 2, 3]}
    new_dict = simple_delete(a_dictionary, 'track')
    print_sorted_dictionary(a_dictionary)
    print("--")
    print_sorted_dictionary(new_dict)

    print("--")
    print("--")
    new_dict = simple_delete(a_dictionary, 'c_is_fun')
    print_sorted_dictionary(a_dictionary)
    print("--")
    print_sorted_dictionary(new_dict)
