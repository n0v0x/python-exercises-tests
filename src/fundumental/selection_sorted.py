"""Module with selection sort for input list"""
__author__ = "Victoria Chetveruhina"
__email__ = "v.chetveruhina@yandex.ru"

import sys


MAX_ATTEMPTS = 3

class InputError(Exception):
    """Exception raised for errors in the input."""
    pass


def parse_from_input() -> list[str]:
    """Read whitespace-separated token from stdin.

    Return:
        A list of strings, one string per token
    """
    input_str = input().split()
    return input_str


def parse_from_argv() -> list[str]:
    """Read whitespace-separated token from sys.argv.

    Return:
        A list of strings, one strings per token.
        Empty, if no argument provided
    """
    input_str = sys.argv[1:]
    return input_str


def string_to_int(input_str: list[str]) -> list[int]:
    """Convert a list of numeric strings to a list of integers.

    Args:
        input_str: A list of numeric strings.
    Returns:
          A list of integers.
    Raises:
          ValueError: If input_str contains non-numeric characters.
    """
    input_list = []

    for i in input_str:
        input_list.append(int(i))
    return input_list

def get_numbers() -> list[int]:
    """Get numbers from argv, or from stdin if argv is empty.

    Return:
         A list of integers.
    """
    input_str_argv = parse_from_argv()

    if input_str_argv:
        try:
            input_list = string_to_int(input_str_argv)
            return input_list
        except ValueError:
            print("Only numbers are allowed.")
    else:
        attempts_left = MAX_ATTEMPTS
        while attempts_left > 0:
            print("Enter the list of numbers:")
            input_str = parse_from_input()

            if not input_str:
                print("Error: List must not be empty.")
                attempts_left -= 1
                continue

            try:
                input_list = string_to_int(input_str)
                return input_list
            except ValueError:
                print("Error: Only numbers are allowed.")
                attempts_left -= 1
        return []


def selection_sort(input_list: list[int]) -> None:
    """Sort the list in place by selection sort.

    Args:
        input_list: A list of integers.

    Return: None
    """
    for i in range(len(input_list) - 1):
        index_min = i

        for j in range(i + 1, len(input_list)):
            if input_list[j] < input_list[index_min]:
                index_min = j

        input_list[i], input_list[index_min] = input_list[index_min], input_list[i]


def main():
    """Read the list of numbers from stdin and sort them in place by selection sort."""
    input_list = get_numbers()

    if input_list:
        selection_sort(input_list)

        print("Selection-sorted list:")
        print(input_list)
    else:
        print("No numbers to sort.")


if __name__ == "__main__":
    main()