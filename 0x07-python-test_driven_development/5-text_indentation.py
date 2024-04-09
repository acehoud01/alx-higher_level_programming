#!/usr/bin/python3


def text_indentation(text):
    """
        Prints the text with 2 new lines after each occurrence.
        of '.', '?', and ':'.

        Args:
            text (str): The input text.

        Raises:
            TypeError: If text is not a string.
        """

    if type(text) is not str:
        raise TypeError("text must be a string")

    for delimit in ".:?":
        text = (delimit + "\n\n").join(
            [line.strip(" ") for line in text.split(delimit)])

    print("{}".format(text), end="")
