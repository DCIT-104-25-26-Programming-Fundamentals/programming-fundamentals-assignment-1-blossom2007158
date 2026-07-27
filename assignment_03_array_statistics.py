# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
##!/usr/bin/env python3
"""
Array Statistics Calculator
Implements sum, average, maximum, and minimum calculations without using
Python's built-in sum(), max(), or min() functions.
"""

import sys


def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    return calculate_sum(numbers) / len(numbers)


def calculate_maximum(numbers):
    # assume list is non-empty when called
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum


def calculate_minimum(numbers):
    # assume list is non-empty when called
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum


def format_number(value):
    # Print integers without a trailing .0, keep floats otherwise
    if isinstance(value, float):
        if value.is_integer():
            return str(int(value))
        else:
            # remove unnecessary trailing zeros while keeping a readable format
            return str(value).rstrip('0').rstrip('.') if '.' in str(value) else str(value)
    return str(value)


def main():
    try:
        n = int(input("How many numbers? "))
    except ValueError:
        print("Error: invalid input for number of items.")
        return

    if n <= 0:
        print("Error: number of items must be a positive integer.")
        return

    numbers = []
    for i in range(1, n + 1):
        try:
            # Accept floats and integers
            value = float(input(f"Enter number {i}: "))
        except ValueError:
            print("Error: invalid number entered.")
            return
        numbers.append(value)

    s = calculate_sum(numbers)
    avg = calculate_average(numbers)
    mx = calculate_maximum(numbers)
    mn = calculate_minimum(numbers)

    print("\nResults:")
    # align the values similar to the example output
    print(f"Sum:     {format_number(s)}")
    print(f"Average: {format_number(avg)}")
    print(f"Maximum: {format_number(mx)}")
    print(f"Minimum: {format_number(mn)}")


if __name__ == "__main__":
    main()

