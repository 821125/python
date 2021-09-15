from abc import abstractmethod


class Textile:
    def __init__(self, size, height):
        self.size = size
        self.height = height

    @abstractmethod
    def sewing(self):
        pass


class Coat(Textile):
    @property
    def sewing(self):
        return round(self.size / 6.5 + 0.5, 2)


class Jacket(Textile):
    @property
    def sewing(self):
        return round(2 * self.height + 0.3, 2)


coat = Coat(48, 3)
jacket = Jacket(54, 3)
print(f'consumption of fabric on the coat = {coat.sewing}')
print(f'consumption of fabric on the jacket = {jacket.sewing}')
print(f'total fabric consumption = {coat.sewing + jacket.sewing}')
