class Matrix:
    class InsertionError(Exception):
        pass

    # contructor matrix
    def __init__(self, a, b):
        self.rows = a
        self.columns = b
        self.matrix = []

    # function to subtract matrices
    def __subtract__(self, matrixB):
        assert self.rows == matrixB.rows and self.columns == matrixB.columns
        result = Matrix(self.rows, self.columns)
        for row1, row2 in zip(self.matrix, matrixB.matrix):
            row = []
            for index1, index2 in zip(row1, row2):
                row.append(index1 - index2)
            result.matrix.append(row)
        return result

    # function to add matrices a+b
    def __add__(self, matrixB):
        assert self.rows == matrixB.rows and self.columns == matrixB.columns
        result = Matrix(self.rows, self.columns)
        for row1, row2 in zip(self.matrix, matrixB.matrix):
            row = []
            for index1, index2 in zip(row1, row2):
                row.append(index1 + index2)
            result.matrix.append(row)
        return result

    def __str__(self):
        return "\n".join([" ".join([str(round(x, 3)) for x in row]) for row in self.matrix])

    def read(self):
        for _ in range(self.rows):
            row = [float(x) if "." in x else int(x)
                for x in input().split()]
            if len(row) != self.columns:
                raise self.InsertionError
            self.matrix.append(row)

    # function to multiply matrices
    def __mul__(self, other):
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


def product(row, col):
    return sum([row[index] * col[index] for index in range(len(row))])


# main program
while True:
    try:
        print("1. Add matrices\n2. Multiply matrices\n3. Subtract matrices\n0. Exit")
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
        elif choice == "3":  # subtract two matrices
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
