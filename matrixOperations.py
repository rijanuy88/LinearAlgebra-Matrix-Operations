class Matrix:
    class InsertionError(Exception):
        pass

    def __init__(self, n, m):
        self.rows = n
        self.columns = m
        # it will be a list of rows where each row is a list of cells (int/float)
        self.matrix = []

    def __subtract__(self, matrixB):
        """returns self matrix - other matrix"""
        assert self.rows == matrixB.rows and self.columns == matrixB.columns  # check if correct dimensions
        result = Matrix(self.rows, self.columns)
        for row1, row2 in zip(self.matrix, matrixB.matrix):
            row = []
            for cell1, cell2 in zip(row1, row2):
                row.append(cell1 - cell2)
            result.matrix.append(row)
        return result

    def __add__(self, matrixB):
        """returns self matrix + other matrix"""
        assert self.rows == matrixB.rows and self.columns == matrixB.columns  # check if correct dimensions
        result = Matrix(self.rows, self.columns)
        for row1, row2 in zip(self.matrix, matrixB.matrix):
            row = []
            for cell1, cell2 in zip(row1, row2):
                row.append(cell1 + cell2)
            result.matrix.append(row)
        return result

    def __str__(self):
        """returns a string representation of the matrix to be printed out"""
        return "\n".join([" ".join([str(round(x, 3)) for x in row]) for row in self.matrix])

    def read(self):
        """reads and fills a matrix from the input"""
        for _ in range(self.rows):
            row = [float(x) if "." in x else int(x)
                   for x in input().split()]  # read a full row
            if len(row) != self.columns:
                raise self.InsertionError  # incorrect input
            self.matrix.append(row)

    def __mul__(self, other):
        """returns matrix * matrix"""
        assert self.columns == other.rows  # check if correct dimensions
        result = Matrix(self.rows, other.columns)
        for i in range(self.rows):
            row = []
            for j in range(other.columns):
                row.append(product(self.matrix[i], other.column(j)))
            result.matrix.append(row)
        return result

    def column(self, index):
        """returns the column at the specified index [0, len["""
        return [x[index] for x in self.matrix]


def product(row, column):
    """returns the result of the dot product of two equally length lists (a row and a column)"""
    return sum([row[index] * column[index] for index in range(len(row))])


# main program
while True:
    try:
        print("1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n4. Subtract matrices\n5. Calculate a determinant\n6. Inverse matrix\n0. Exit")
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
        elif choice == "2":  # multiply two matrices
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
        elif choice == "4":  # subtract two matrices
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
        elif choice == "0":  # exit
            break
    except AssertionError:
        print("The operation cannot be performed.")
    except (Matrix.InsertionError, ValueError):
        print("WRONG INPUT")
    print("\n")
