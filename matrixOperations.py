# Programming Project 2 - Different Operations on Matrices
# Group 1-CS3A - Castillon, Ignas, Wong
'''
This program allows the user to choose from a variety of matrix operations. 
In order to perform these matrix operations, the program, takes in the size of each matrix and parses the matrixes into arrays, which 
are then put through specific functions in order to prodice teh chosen outputs.
'''

'''
Sample output:
1. Add matrices
2. Subtract matrices
3. Multiply matrices
0. Exit
Your choice: 1
Enter size of first matrix: 2 2
Enter first matrix:
1 2
4 5
Enter size of second matrix: 2 2
Enter second matrix:
5 6
8 9
The result is:
6 8
12 14


1. Add matrices
2. Subtract matrices
3. Multiply matrices
0. Exit
Your choice: 2
Enter size of first matrix: 2 2
Enter first matrix:
5 6
8 9
Enter size of second matrix: 2 2
Enter second matrix:
1 2 
4 5
The result is:
4 4
4 4


1. Add matrices
2. Subtract matrices
3. Multiply matrices
0. Exit
Your choice: 3
Enter size of first matrix: 2 2
Enter first matrix:
5 6
8 9
Enter size of second matrix: 2 2
Enter second matrix:
1 2
4 5
The result is:
29 40
44 61


1. Add matrices
2. Subtract matrices
3. Multiply matrices
0. Exit
Your choice: 0
'''


class Matrix:
    class InsertionError(Exception):
        pass

    # Constructor function
    # This function is for initializing variables and array
    def __init__(self, a, b):
        self.rows = a
        self.columns = b
        self.matrix = []

    # Function to subtract matrices
    # The subtraction of two matrices Am*n and Bm*n gives a matrix Cm*n.
    def __subtract__(self, matrixB):
        assert self.rows == matrixB.rows and self.columns == matrixB.columns
        result = Matrix(self.rows, self.columns)
        for row1, row2 in zip(self.matrix, matrixB.matrix):
            row = []
            for index1, index2 in zip(row1, row2):
                row.append(index1 - index2)
            result.matrix.append(row)
        return result

    # Function to add matrices a+b
    # The addition of two matrices Amxn and Bmxn gives a matrix Cmxn.
    def __add__(self, matrixB):
        assert self.rows == matrixB.rows and self.columns == matrixB.columns
        result = Matrix(self.rows, self.columns)
        for row1, row2 in zip(self.matrix, matrixB.matrix):
            row = []
            for index1, index2 in zip(row1, row2):
                row.append(index1 + index2)
            result.matrix.append(row)
        return result

    # Function to multiply matrices
    # The multiplication of two matrices Am*n and Bn*p gives a matrix Cm*p.
    def __mul__(self, other):
        # s number of columns in A must be equal to number of rows in B to calculate C = A*B.
        assert self.columns == other.rows
        result = Matrix(self.rows, other.columns)
        for i in range(self.rows):
            row = []
            for j in range(other.columns):
                row.append(product(self.matrix[i], other.column(j)))
            result.matrix.append(row)
        return result

    def column(self, i):
        return [x[i] for x in self.matrix]
    # Function to present matrices as string values

    def __str__(self):
        # string representation of the matrix to be printed out
        return "\n".join([" ".join([str(round(x, 3)) for x in row]) for row in self.matrix])

    def read(self):
        # reads and fills a matrix from the input
        # _ stores  stores the value of the last expression automatically
        for _ in range(self.rows):
            row = [float(x) if "." in x else int(x) for x in input().split()]
            if len(row) != self.columns:
                raise self.InsertionError
            self.matrix.append(row)


def product(row, col):
    return sum([row[index] * col[index] for index in range(len(row))])


# Main program
# This gives the user a set of choices for matrix operations
while True:
    try:
        print("1. Add matrices\n2. Subtract matrices\n3. Multiply matrices\n0. Exit")
        choice = input("Your choice: ")

        if choice == "1":  # add two matrices
            a_row, a_column = input("Enter size of first matrix: ").split()
            A = Matrix(int(a_row), int(a_column))
            print("Enter first matrix:")
            A.read()
            b_row, b_column = input("Enter size of second matrix: ").split()
            B = Matrix(int(b_row), int(b_column))
            print("Enter second matrix:")
            B.read()
            print("The result is:")
            print(A + B)

        elif choice == "2":  # subtract two matrices
            a_row, a_column = input("Enter size of first matrix: ").split()
            A = Matrix(int(a_row), int(a_column))
            print("Enter first matrix:")
            A.read()
            b_row, b_column = input("Enter size of second matrix: ").split()
            B = Matrix(int(b_row), int(b_column))
            print("Enter second matrix:")
            B.read()
            print("The result is:")
            print(A.__subtract__(B))

        elif choice == "3":  # multiply two matrices
            a_row, a_column = input("Enter size of first matrix: ").split()
            A = Matrix(int(a_row), int(a_column))
            print("Enter first matrix:")
            A.read()
            b_row, b_column = input("Enter size of second matrix: ").split()
            B = Matrix(int(b_row), int(b_column))
            print("Enter second matrix:")
            B.read()
            print("The result is:")
            print(A * B)

        elif choice == "0":  # exit
            break

    except AssertionError:
        print("The operation cannot be performed.")
    except (Matrix.InsertionError, ValueError):
        print("WRONG INPUT")
    print("\n")
