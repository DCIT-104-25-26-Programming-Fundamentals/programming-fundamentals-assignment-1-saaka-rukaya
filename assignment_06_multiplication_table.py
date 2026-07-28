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
# =============================================================================

def print_single_table(number):
    print("\nMultiplication Table for", number)

    for multiplier in range(1, 13):
        answer = number * multiplier
        print(number, "x", multiplier, "=", answer)


def print_multiple_tables(number_of_tables):
    if number_of_tables <= 0:
        print("Error: N must be a positive integer.")
        return

    for table_number in range(1, number_of_tables + 1):
        print("\nMultiplication Table for", table_number)

        for multiplier in range(1, 13):
            answer = table_number * multiplier
            print(table_number, "x", multiplier, "=", answer)

        print("---------------------------")


def main():
    # Part A
    number = int(input("Enter a number for its multiplication table: "))
    print_single_table(number)

    # Part B
    number_of_tables = int(input("\nEnter N to print tables from 1 to N: "))

    if number_of_tables <= 0:
        print("Error: N must be a positive integer.")
        return

    print_multiple_tables(number_of_tables)


main()