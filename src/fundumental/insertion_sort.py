"""Module with insertion sort for input list"""
__author__ = "Victoria Chetveruhina"
__email__ = "v.chetveruhina@yandex.ru"

import sys


MAX_ATTEMPTS = 3


def parse_from_input() -> list[str]:
    """Parse the user input from stdin and return a list of the numeric strings.

    Returns:
        A list of numeric strings.
    """
    return input().split()


def parse_from_argv() -> list[str]:
    """Parse the user input from command line and return a list of numeric strings.

    Returns:
        A list of numeric strings.
        Empty if no arguments are provided.
    """
    return sys.argv[1:]


def strings_to_ints(input_strs: list[str]) -> list[int]:
    """Convert the numeric strings from input to an integer.

    Args:
        input_strs: A list of numeric strings.

    Returns:
        A list of integers.
    """
    return [int(item) for item in input_strs]


def get_numbers() -> list[int]:
    """Get a list of integers from user input or command line and convert them to numeric values.

    Returns:
        A list of integers.
    """
    input_strs_argv = parse_from_argv()

    if input_strs_argv:
        try:
            return strings_to_ints(input_strs_argv)
        except ValueError:
            print("Only numbers are allowed.")
            return []
    else:
        attempts_left = MAX_ATTEMPTS

        while attempts_left > 0:
            print("Enter the list of numbers:")
            input_strs_stdin = parse_from_input()

            if not input_strs_stdin:
                print("Error: List must not be empty.")
                attempts_left -= 1
                continue

            try:
                return strings_to_ints(input_strs_stdin)
            except ValueError:
                print("Error: Only numbers are allowed.")
                attempts_left -= 1
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
        print(*input_list)
    else:
        print("No numbers to sort.")


if __name__ == "__main__":
    main()
