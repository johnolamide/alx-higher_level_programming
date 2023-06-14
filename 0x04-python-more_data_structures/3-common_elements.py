#!/usr/bin/python3
def common_elements(set_1, set_2):
    """finds common elements in two sets

    Args:
        set_1: first set
        set_2: second set

    Returns:
        common element(s)
    """
    return set_1 & set_2


if __name__ == "__main__":
    set_1 = {"Python", "C", "Javascript"}
    set_2 = {"Bash", "C", "Ruby", "Perl"}
    c_set = common_elements(set_1, set_2)
    print(sorted(list(c_set)))
