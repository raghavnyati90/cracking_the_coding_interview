"""Is Unique: Implement an algorithm to determine if a string has all
unique characters. What if you cannot use additional data structures?"""


def is_unique(input_str: str) -> bool:
    """
    To check if a string has all unique characters
    :param input_str: input string
    :return: True if string has all unique characters
    """

    if not input_str:
        return False

    for i in range(0, len(input_str)-1):
        if input_str[i] in input_str[i+1:]:
            return False
    return True


def is_unique_with_data_structure(input_str: str) -> bool:
    """
    To check if a string has all unique characters
    :param input_str: input string
    :return: True if string has all unique characters
    """

    if not input_str:
        return False

    letters = {}

    for letter in input_str:
        if letter in letters:
            return False
        letters[letter] = True

    return True


if __name__ == '__main__':
    print(is_unique("1234321"))
    print(is_unique_with_data_structure("1234321"))
    print(is_unique(""))
    print(is_unique_with_data_structure(""))
    print(is_unique("asdf"))
    print(is_unique_with_data_structure("asdf"))
    print(is_unique("1"))
    print(is_unique_with_data_structure("1"))
