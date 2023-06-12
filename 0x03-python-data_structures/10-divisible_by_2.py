#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Finds all multiples of 2 in a list

    Args:
       my_list: list of integers

    Returns:
        list containing True or False
    """
    if not my_list:
        return None
    new_list = [i % 2 == 0 for i in my_list]
    return new_list


if __name__ == "__main__":
    my_list = [0, 1, 2, 3, 4, 5, 6]
    list_result = divisible_by_2(my_list)

    i = 0
    while i < len(list_result):
        print("{:d} {:s} divisible by 2"
              .format(my_list[i], "is" if list_result[i] else "is not"))
        i += 1
