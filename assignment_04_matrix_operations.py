# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def read_matrix(number_of_rows, number_of_columns, matrix_name):
    matrix = []

    print("\nEnter values for Matrix", matrix_name)

    for row_index in range(number_of_rows):
        while True:
            row_values = input(
                "Enter row " + str(row_index + 1) + ": "
            ).split()

            if len(row_values) == number_of_columns:
                row = []

                for value in row_values:
                    row.append(float(value))

                matrix.append(row)
                break
            else:
                print(
                    "Error: Please enter exactly",
                    number_of_columns,
                    "values."
                )

    return matrix


def display_matrix(matrix):
    for row in matrix:
        for value in row:
            print(f"{value:8g}", end=" ")
        print()


def transpose_matrix(matrix):
    number_of_rows = len(matrix)
    number_of_columns = len(matrix[0])

    transposed_matrix = []

    for column_index in range(number_of_columns):
        new_row = []

        for row_index in range(number_of_rows):
            new_row.append(matrix[row_index][column_index])

        transposed_matrix.append(new_row)

    return transposed_matrix


def add_matrices(first_matrix, second_matrix):
    number_of_rows = len(first_matrix)
    number_of_columns = len(first_matrix[0])

    result_matrix = []

    for row_index in range(number_of_rows):
        new_row = []

        for column_index in range(number_of_columns):
            value = (
                first_matrix[row_index][column_index]
                + second_matrix[row_index][column_index]
            )

            new_row.append(value)

        result_matrix.append(new_row)

    return result_matrix


def multiply_matrices(first_matrix, second_matrix):
    first_matrix_rows = len(first_matrix)
    first_matrix_columns = len(first_matrix[0])
    second_matrix_columns = len(second_matrix[0])

    result_matrix = []

    for row_index in range(first_matrix_rows):
        new_row = []

        for column_index in range(second_matrix_columns):
            total = 0

            for position in range(first_matrix_columns):
                total = total + (
                    first_matrix[row_index][position]
                    * second_matrix[position][column_index]
                )

            new_row.append(total)

        result_matrix.append(new_row)

    return result_matrix


def main():
    # Part A: Transpose a matrix
    print("PART A - TRANSPOSE A MATRIX")

    number_of_rows = int(input("Enter number of rows: "))
    number_of_columns = int(input("Enter number of columns: "))

    if number_of_rows <= 0 or number_of_columns <= 0:
        print("Error: Matrix dimensions must be positive integers.")
        return

    original_matrix = read_matrix(
        number_of_rows,
        number_of_columns,
        "A"
    )

    transposed_matrix = transpose_matrix(original_matrix)

    print("\nOriginal Matrix:")
    display_matrix(original_matrix)

    print("\nTransposed Matrix:")
    display_matrix(transposed_matrix)

    # Part B: Add two matrices
    print("\nPART B - ADD TWO MATRICES")

    number_of_rows = int(input("Enter number of rows: "))
    number_of_columns = int(input("Enter number of columns: "))

    if number_of_rows <= 0 or number_of_columns <= 0:
        print("Error: Matrix dimensions must be positive integers.")
        return

    first_matrix = read_matrix(
        number_of_rows,
        number_of_columns,
        "A"
    )

    second_matrix = read_matrix(
        number_of_rows,
        number_of_columns,
        "B"
    )

    sum_matrix = add_matrices(first_matrix, second_matrix)

    print("\nMatrix A:")
    display_matrix(first_matrix)

    print("\nMatrix B:")
    display_matrix(second_matrix)

    print("\nSum of Matrix A and Matrix B:")
    display_matrix(sum_matrix)

    # Part C: Multiply two matrices
    print("\nPART C - MULTIPLY TWO MATRICES")

    matrix_a_rows = int(input("Enter number of rows for Matrix A: "))
    matrix_a_columns = int(input("Enter number of columns for Matrix A: "))

    matrix_b_rows = int(input("Enter number of rows for Matrix B: "))
    matrix_b_columns = int(input("Enter number of columns for Matrix B: "))

    if (
        matrix_a_rows <= 0
        or matrix_a_columns <= 0
        or matrix_b_rows <= 0
        or matrix_b_columns <= 0
    ):
        print("Error: Matrix dimensions must be positive integers.")
        return

    if matrix_a_columns != matrix_b_rows:
        print(
            "Error: The number of columns in Matrix A must equal",
            "the number of rows in Matrix B."
        )
        return

    matrix_a = read_matrix(
        matrix_a_rows,
        matrix_a_columns,
        "A"
    )

    matrix_b = read_matrix(
        matrix_b_rows,
        matrix_b_columns,
        "B"
    )

    product_matrix = multiply_matrices(matrix_a, matrix_b)

    print("\nMatrix A:")
    display_matrix(matrix_a)

    print("\nMatrix B:")
    display_matrix(matrix_b)

    print("\nProduct of Matrix A and Matrix B:")
    display_matrix(product_matrix)


main()