"""Module with insertion sort for input list"""
__author__ = "Victoria Chetverukhina"
__email__ = "v.chetveruhina@yandex.ru"

import sys


MAX_ATTEMPTS = 3

class InputError(Exception):
    """Exception raised for errors in the input."""
    pass

def parse_from_input() -> list[str]:
    """Read whitespace-separated tokens from stdin.

    Returns:
        A list of strings, one string per token.
    """
    input_str = input().split()
    return input_str


def parse_from_argv() -> list[str]:
    """Read whitespace-separated tokens from argv.

    Returns:
        A list of strings, one string per token.
        Empty if no arguments provided.
    """
    input_str = sys.argv[1:]
    return input_str


def strings_to_numbers(input_str: list[str]) -> list[int]:
    """Convert a list of numeric strings to a list of integers.

    Args:
        input_str: A list of strings, each string is a numeric value.

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
    """Get numbers from avg, or from stdin if argv is empty.

    Returns:
         A list of integers.
    """
    input_str_argv = parse_from_argv()

    if input_str_argv:
        try:
            input_list = strings_to_numbers(input_str_argv)
            return input_list
        except ValueError:
            print("Only numbers are allowed.")
    else:
        attempt_left = MAX_ATTEMPTS
        while attempt_left > 0:
            print("Enter the list of numbers:")
            input_str = parse_from_input()

            if not input_str:
                print("Error: List must not be empty.")
                attempt_left -= 1
                continue

            try:
                input_list = strings_to_numbers(input_str)
                return input_list
            except ValueError:
                print("Error: Only numbers are allowed.")
                attempt_left -= 1
        return []


def insertion_sort(input_list: list[int]) -> None:
    """Sort the list in place by insertion sort.

    Args:
        input_list: A list of integers. Modified in place.

    Returns: None
    """
    for i in range(1, len(input_list)):
        key = input_list[i]
        j = i - 1
        while j >= 0 and input_list[j] > key:
            input_list[j + 1] = input_list[j]
            j -= 1
        input_list[j + 1] = key


def main():
    """Read list of integers from stdin or argv, sort by insertion sort and print."""
    input_list = get_numbers()

    if input_list:
        insertion_sort(input_list)

        print("Insertion-sorted list:")
        print(input_list)
    else:
        print("No numbers to sort.")


if __name__ == "__main__":
    main()
