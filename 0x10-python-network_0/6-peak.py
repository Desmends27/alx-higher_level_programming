#!/usr/bin/python3
"""Find the peak element in a node"""


def find_peak(list_of_integers):
    """Return the index of the peak element"""

    # Using binary search
    left, right = 0, len(list_of_integers) - 1

    # While loop to return inside (left <= right)
    while left <= right:
        # Set mid to avoid overflow
        mid = left + ((right - left) // 2)

        # Check left element
        if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            # Move right
            right = mid - 1
        elif (
            mid < len(list_of_integers) - 1
            and list_of_integers[mid] < list_of_integers[mid + 1]
        ):
            # Move left
            left = mid + 1
        else:
            return list_of_integers[mid]
