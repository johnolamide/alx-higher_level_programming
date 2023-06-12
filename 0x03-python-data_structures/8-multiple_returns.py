#!/usr/bin/python3
def multiple_returns(sentence):
    """Returns a tuple with the len of its string and its characters

    Args:
        sentence: string variable

    Returns:
        tuple containing length and characters
    """
    if not sentence:
        return (0, None)
    else:
        return (len(sentence), sentence[0])


if __name__ == "__main__":
    sentence = "At school, I learnt C!"
    length, first = multiple_returns(sentence)
    print("Length: {:d} - First character: {}".format(length, first))
