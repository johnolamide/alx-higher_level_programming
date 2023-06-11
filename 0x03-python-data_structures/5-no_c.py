#!/usr/bin/python3
def no_c(my_string):
    """Removes all characters 'c' and 'C'

    Args:
        my_string: string statement

    Returns:
        The modified string
    """
    new_string = ''
    for char in my_string:
        if ((char != 'c') and (char != 'C')):
            new_string += char
    return new_string


if __name__ == "__main__":
    print(no_c("Best School"))
    print(no_c("Chicago"))
    print(no_c("C is fun!"))
