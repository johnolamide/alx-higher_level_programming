#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """set of elements present in only one set

    Args:
        set_1: first set
        set_2: second set

    Returns:
        new set
    """
    return set_1 ^ set_2


if __name__ == "__main__":
    set_1 = {"Python", "C", "Javascript"}
    set_2 = {"Bash", "C", "Ruby", "Perl"}
    od_set = only_diff_elements(set_1, set_2)
    print(sorted(list(od_set)))
