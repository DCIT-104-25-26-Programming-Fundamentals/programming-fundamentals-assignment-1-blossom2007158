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
#

def read_matrix(rows, cols):
    """Read a matrix from user input."""
    matrix = []
    for i in range(rows):
        while True:
            try:
                row = list(map(float, input(f"Enter row {i + 1}: ").split()))
                if len(row) != cols:
                    print(f"Error: Please enter exactly {cols} values.")
                    continue
                matrix.append(row)
                break
            except ValueError:
                print("Error: Please enter valid numbers separated by spaces.")
    return matrix


def display_matrix(matrix, title="Matrix"):
    """Display a matrix in neat, aligned grid format."""
    print(f"\n{title}:")
    if not matrix:
        print("(Empty matrix)")
        return
    
    # Calculate column widths
    col_widths = []
    for col in range(len(matrix[0])):
        max_width = 0
        for row in matrix:
            max_width = max(max_width, len(f"{row[col]:.1f}"))
        col_widths.append(max_width)
    
    # Print rows
    for row in matrix:
        row_str = ""
        for i, val in enumerate(row):
            row_str += f"{val:>{col_widths[i]}.1f}  "
        print(row_str)


def transpose_matrix(matrix):
    """
    PART A — Transpose a Matrix
    Compute and return the transpose (rows become columns, columns become rows).
    """
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    
    transposed = []
    for col in range(cols):
        new_row = []
        for row in range(rows):
            new_row.append(matrix[row][col])
        transposed.append(new_row)
    
    return transposed


def add_matrices(matrix_a, matrix_b):
    """
    PART B — Add Two Matrices
    Compute and return the element-wise sum of two matrices of the same size.
    """
    rows = len(matrix_a)
    cols = len(matrix_a[0])
    
    result = []
    for i in range(rows):
        new_row = []
        for j in range(cols):
            new_row.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(new_row)
    
    return result


def multiply_matrices(matrix_a, matrix_b):
    """
    PART C — Multiply Two Matrices
    Compute and return the matrix product A × B.
    A is M x N and B is N x P; result is M x P.
    """
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0]) if rows_a > 0 else 0
    rows_b = len(matrix_b)
    cols_b = len(matrix_b[0]) if rows_b > 0 else 0
    
    if cols_a != rows_b:
        print("Error: Number of columns in A must equal number of rows in B.")
        return None
    
    result = []
    for i in range(rows_a):
        new_row = []
        for j in range(cols_b):
            value = 0
            for k in range(cols_a):
                value += matrix_a[i][k] * matrix_b[k][j]
            new_row.append(value)
        result.append(new_row)
    
    return result


def main():
    """Main program to run all matrix operations."""
    print("=" * 60)
    print("MATRIX OPERATIONS")
    print("=" * 60)
    
    while True:
        print("\nChoose an operation:")
        print("1. Transpose a Matrix")
        print("2. Add Two Matrices")
        print("3. Multiply Two Matrices")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            print("\n--- TRANSPOSE A MATRIX ---")
            m = int(input("Enter number of rows: "))
            n = int(input("Enter number of columns: "))
            matrix = read_matrix(m, n)
            display_matrix(matrix, "Original Matrix")
            transposed = transpose_matrix(matrix)
            display_matrix(transposed, "Transposed Matrix")
        
        elif choice == "2":
            print("\n--- ADD TWO MATRICES ---")
            m = int(input("Enter number of rows: "))
            n = int(input("Enter number of columns: "))
            print("\nEnter Matrix A:")
            matrix_a = read_matrix(m, n)
            print("\nEnter Matrix B:")
            matrix_b = read_matrix(m, n)
            display_matrix(matrix_a, "Matrix A")
            display_matrix(matrix_b, "Matrix B")
            result = add_matrices(matrix_a, matrix_b)
            display_matrix(result, "A + B")
        
        elif choice == "3":
            print("\n--- MULTIPLY TWO MATRICES ---")
            m = int(input("Enter rows in Matrix A: "))
            n = int(input("Enter columns in Matrix A (= rows in Matrix B): "))
            p = int(input("Enter columns in Matrix B: "))
            print("\nEnter Matrix A:")
            matrix_a = read_matrix(m, n)
            print("\nEnter Matrix B:")
            matrix_b = read_matrix(n, p)
            display_matrix(matrix_a, "Matrix A")
            display_matrix(matrix_b, "Matrix B")
            result = multiply_matrices(matrix_a, matrix_b)
            if result:
                display_matrix(result, "A × B")
        
        elif choice == "4":
            print("\nGoodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
