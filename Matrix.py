#Matrix class to identify location within the strike zone
class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [[0] * cols for _ in range(rows)]

    def populate_matrix(self):
        count = 1
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j] = count
                count += 1

    def get_position(self, value):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.matrix[i][j] == value:
                    return i, j
        return None

    def display_matrix(self):
        for row in self.matrix:
            print(row)


if __name__ == "__main__":
    # Create a 5x5 matrix
    matrix_size = 5
    my_matrix = Matrix(matrix_size, matrix_size)

    # Populate the matrix with labeled positions
    my_matrix.populate_matrix()

    # Display the matrix
    print("Matrix:")
    my_matrix.display_matrix()

    # Example: Get the position of value 12
    value_to_find = 12
    position = my_matrix.get_position(value_to_find)

    if position:
        print(f"\nThe position of {value_to_find} in the matrix is: {position}")
    else:
        print(f"\n{value_to_find} not found in the matrix.")