#!/usr/bin/python3
def raise_exception_msg(message=""):
    """raise a name exception with a message

    Args:
        message: message to display with exception

    Returns:
        exception with message
    """
    if message:
        raise NameError(message)


if __name__ == "__main__":
    try:
        raise_exception_msg("C is fun")
    except NameError as ne:
        print(ne)
