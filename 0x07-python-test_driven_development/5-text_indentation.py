#!/usr/bin/python3
"""
    Module contains: text_indentation function
"""


def text_indentation(text):
    """ function that prints a text with 2 new lines after
        each of the characters . ? :

        Args:
            text (str): text to print

        Raises:
            TypeError: if text is not a string
    """
    if (type(text) != str):
        raise TypeError("text must be a string")
    text = text.strip()
    new_text = ""
    skip_space = False
    for char in text:
        if skip_space and char == ' ':
            skip_space = False
            continue
        new_text += char
        if char in ['.', '?', ':']:
            new_text += '\n\n'
            skip_space = True
    print(new_text)


if __name__ == "__main__":
    text_indentation("""Lorem ipsum dolor sit amet, \
consectetur adipiscing elit. \
Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
beatiorem! Iam ruinas videres""")
