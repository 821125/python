class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} is started with speed {self.speed}'

    def stop(self):
        return f'{self.name} is stopped'

    def turn(self, direction):
        lst = ['left', 'right']
        if direction not in lst:
            return '\033[31merror, direction can only be "left" or "right"\033[0m'
        else:
            return f'{self.name} is turned {direction}'

    def show_speed(self):
        return f'current speed {self.name} is {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\033[33mspeed of {self.name} is higher than allowed for town car\033[0m'
        else:
            return f'speed of {self.name} is normal'


class SportCar(Car):
    def show_speed(self):
        if self.speed < 100:
            return f'{self.name} is capable of more than that'
        else:
            return f'{self.name} it is very nice'


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\033[33mspeed of {self.name} is higher than allowed for work car\033[0m'
        else:
            return f'speed of {self.name} is normal'


class PoliceCar(Car):
    def check_police(self):
        if self.is_police:
            return f'{self.name} is a special police car'
        else:
            return f'{self.name} is not a special police car'


honda = SportCar(95, 'red', 'honda', False)
renault = TownCar(65, 'white', 'renault', False)
ford = PoliceCar(110, 'blue', 'ford', True)
chevrolet = WorkCar(75, 'magenta', 'chevrolet', True)

print(f'{honda.color} {honda.name} speed {honda.speed}')
print(honda.show_speed())
print(honda.turn('left'))
print(honda.turn('west'))
print(renault.go(), renault.show_speed(), sep='\n')
print(ford.show_speed())
print(ford.check_police())
