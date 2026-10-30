"""Solves the Two Sum problem by checking every possible pair."""

from itertools import combinations

def two_sum_brute_force(self, nums: list[int], target: int) -> list[int]:
    """Return the indices of two elements whose sum equals `target`.

    Checks every unique pair until the first matching pair is found.
    The same element cannot be used twice.

     Args:
        nums: A list of integers.
        target: The required sum of two elements.

    Returns:
        The indices of the first matching pair.

    Complexity:
        Time: O(n²).
        Extra space: O(1).
    """
    for (first_index, first), (second_index, second) in combinations(
        enumerate(nums), 2
    ):
        if first + second == target:
            return [first_index, second_index]

solution = BruteForceSolution()

result = solution.two_sum_brute_force([2, 7, 11, 15], 9)
print(result)

