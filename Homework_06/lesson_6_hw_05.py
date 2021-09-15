class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'start rendering'


class Pen(Stationary):
    def draw(self):
        return f'start drawing thin blue {self.title}'


class Pencil(Stationary):
    def draw(self):
        return f'start drawing grey {self.title}'


class Handle(Stationary):
    def draw(self):
        return f'start drawing bold yellow {self.title}'


pen = Pen('line')
pencil = Pencil('circle')
handle = Handle('rectangle')

print(pen.draw(), pencil.draw(), handle.draw(), sep='\n')
