class Matrix:
    def __init__(self, lst_one, lst_two, lst_three):
        self.lst_one = lst_one
        self.lst_two = lst_two
        self.lst_three = lst_three
        self.matrix = [
            lst_one.split(),
            lst_two.split(),
            lst_three.split()
            ]

    def __str__(self):
        return f'{self.lst_one}\n{self.lst_two}\n{self.lst_three}'

    def __add__(self, other):
        total = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(3):
            for j in range(3):
                total[i][j] = int(self.matrix[i][j]) + int(other.matrix[i][j])
        for el in total:
            print(*el)


matrix_one = Matrix('4 5 6', '7 8 9', '1 2 3')
matrix_two = Matrix('4 5 6', '4 1 2', '7 8 9')
print(matrix_one)
print()
print(matrix_two)
print()
matrix_one + matrix_two
