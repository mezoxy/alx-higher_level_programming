#!/usr/bin/python3
"""The module 5-text_indentation"""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.
        Args:
            text(string): The text to be printed
        Return: A new text
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text) and text[i] == ' ':
        i += 1

    while i < len(text):
        print(text[i], end="")
        if text[i] == "\n" or text[i] in ".?:":
            if text[i] in ".?:":
                print("\n")
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
