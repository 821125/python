class Cell:
    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        if self.quantity > other.quantity:
            return self.quantity - other.quantity
        else:
            print(f'{self.quantity} - {other.quantity}: wrong operation')

    def __mul__(self, other):
        return Cell(self.quantity * other.quantity)

    def __truediv__(self, other):
        return Cell(round(self.quantity / other.quantity))

    def make_order(self, per_row):
        rows, tail = self.quantity // per_row, self.quantity % per_row
        return '\n'.join(['*' * per_row] * rows + (["*" * tail] if tail else []))

    def __str__(self):
        return f'The cell consists of {self.quantity} cells.'


cells_one = Cell(25)
cells_two = Cell(14)
print(cells_one)
print(cells_one + cells_two)
print(cells_two - cells_one)
print(cells_two * cells_one)
print(cells_one / cells_two)
print(cells_two.make_order(5))
print(cells_one.make_order(10))
