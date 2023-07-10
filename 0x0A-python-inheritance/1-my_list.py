#!/usr/bin/python3
""" Module contains class definition for MyList
"""


class MyList(list):
    """
        MyList(list): inherits from list
        Methods:
            print_sorted: prints the list sorted
    """

    def print_sorted(self):
        """ prints the sorted list
        """
        print(sorted(self))


if __name__ == "__main__":
    my_list = MyList()
    my_list.append(1)
    my_list.append(4)
    my_list.append(2)
    my_list.append(3)
    my_list.append(5)
    print(my_list)
    my_list.print_sorted()
    print(my_list)
