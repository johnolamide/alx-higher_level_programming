#!/usr/bin/python3
""" This Module contains the function definition for find_peak
"""


def find_peak(list_of_integers):
    """ finds a peak in a list of unsorted integers
        Args:
            list_of_integers: list of unsorted integers
    """
    if not list_of_integers:
        return None

    left = 0
    right = len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return list_of_integers[left]


if __name__ == '__main__':
    """ Test function find_peak """
    find_peak = __import__('6-peak').find_peak

    print(find_peak([1, 2, 4, 6, 3]))
    print(find_peak([4, 2, 1, 2, 3, 1]))
    print(find_peak([2, 2, 2]))
    print(find_peak([]))
    print(find_peak([-2, -4, 2, 1]))
    print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))
