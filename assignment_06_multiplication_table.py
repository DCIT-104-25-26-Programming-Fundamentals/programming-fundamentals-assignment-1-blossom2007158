# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
#
# Write a Python program that generates multiplication tables using loops
# and functions.
#
# -----------------------------------------------------------------------------
# PART A — Single Table
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Print the multiplication table for that number from 1 to 12.
#
# Expected output (if user enters 5):
#
#   Multiplication Table for 5:
#   5  x  1  =  5
#   5  x  2  =  10
#   5  x  3  =  15
#   ...
#   5  x  12 =  60
#
# -----------------------------------------------------------------------------
# PART B — Bonus: Tables from 1 to N
# -----------------------------------------------------------------------------
# - Ask the user to enter a number N.
# - Print the full multiplication table for every number from 1 to N.
# - Add a separator line (e.g. "---") between each table.
#
# Expected output (if user enters 3):
#
#   Multiplication Table for 1:
#   1  x  1  =  1
#   ...
#   1  x  12 =  12
#   ---------------------------
#   Multiplication Table for 2:
#   2  x  1  =  2
#   ...
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - N must be a positive integer. If the user enters an invalid value,
#   print an error message and stop.
# - Each part must be in its own function (see scaffold below).
# - Complete Part A before attempting Part B.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# def multiplication_table(n):
    """Print the multiplication table for a single number from 1 to 12."""
    print(f"Multiplication Table for {n}:")
    for i in range(1, 13):
        result = n * i
        print(f"{n}  x  {i}  =  {result}")


def multiplication_tables(n):
    """Print multiplication tables for numbers 1 to N."""
    for num in range(1, n + 1):
        multiplication_table(num)
        if num < n:
            print("---------------------------")


def main():
    """Main function to handle user input and validation."""
    try:
        # Part A
        num = int(input("Enter a number for the multiplication table: "))
        if num <= 0:
            print("Error: Please enter a positive integer.")
            return
        multiplication_table(num)
        
        # Part B
        print("\n" + "="*50 + "\n")
        choice = input("Would you like to print tables from 1 to N? (yes/no): ").lower()
        if choice == "yes":
            n = int(input("Enter N: "))
            if n <= 0:
                print("Error: Please enter a positive integer.")
                return
            multiplication_tables(n)
    except ValueError:
        print("Error: Please enter a valid positive integer.")


if __name__ == "__main__":
    main()

