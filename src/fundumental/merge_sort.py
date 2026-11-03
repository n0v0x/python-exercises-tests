"""Module with implementation of the merge sort algorithm."""
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


def merge(left: list[int], right: list[int]) -> list[int]:
    """Merge two sorted lists into a single sorted list.

    Args:
        left: A list of integers.
        right: A list of integers.

    Returns:
          A list of integers.
    """
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(input_list: list[int]) -> list[int]:
    """Sorts a given list of integers using merge sort.

    Args:
        input_list: A list of integers.

    Returns:
          A sorted list of integers.
    """
    if len(input_list) <= 1:
        return input_list

    mid = len(input_list) // 2

    left = merge_sort(input_list[:mid])

    right = merge_sort(input_list[mid:])
    return merge(left, right)


def main():
    """Read the list of numbers from user input or command line and sort them using merge sort."""
    input_list = get_numbers()

    if input_list:
        sorted_list = merge_sort(input_list)
        print("Merge-sorted list =", *sorted_list)
    else:
        print("No numbers to sort.")


if __name__ == '__main__':
    main()