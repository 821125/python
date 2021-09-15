class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def calculate(self, thick):
        print(f'Weight of asphalt: {int((self._length * self._width * 25 * thick) / 1000)} t.')


rd = Road(5000, 20)
rd.calculate(5)
