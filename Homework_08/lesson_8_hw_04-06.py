class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


class StoreEquipment:
    def __init__(self):
        self.dict = {}

    def add_to_store(self, equip):
        self.dict.setdefault(equip.auto_count, []).append(equip)
        print(f'\033[32m{equip} -> added to base\033[0m')

    def remover(self, auto_count):
        if self.dict[auto_count]:
            print(f'\033[33mrecording N{auto_count} -> deleted from base\033[0m')
            self.dict.pop(auto_count)

    def show_dict(self):
        print('\033[4mcurrent status:\033[0m')
        for el in self.dict:
            print(*self.dict.get(el))


class Equipment:
    auto_count = 0

    def __init__(self, name, quantity, department):
        try:
            self.name = name
            self.quantity = int(quantity)
            self.department = department
            self.auto_count += 1
        except ValueError:
            print('\033[31mERROR: you entered an invalid value (input integer)')

    def __repr__(self):
        return f'{self.auto_count} - name: {self.name}/ quantity: {self.quantity} pcs. / department: {self.department}'


class Scanner(Equipment):
    def __init__(self, name, quantity, department, resolution):
        super().__init__(name, quantity, department)
        Equipment.auto_count += 1
        self.resolution = resolution

    def __repr__(self):
        return f'{super().__repr__()}/ resolution: {self.resolution} px'


class Printer(Equipment):
    def __init__(self, name, quantity, department, color):
        super().__init__(name, quantity, department)
        Equipment.auto_count += 1
        self.color = color

    def __repr__(self):
        return f'{super().__repr__()}/ color printing: {self.color}'


class CopyMachine(Equipment):
    def __init__(self, name, quantity, department, double_sided):
        super().__init__(name, quantity, department)
        Equipment.auto_count += 1
        self.double_sided = double_sided

    def __repr__(self):
        return f'{super().__repr__()}/ double-sided printing: {self.double_sided}'


store = StoreEquipment()
scanner = Scanner('Kyocera', 2, 'accounting department', 1200)
printer1 = Printer('HP', 5, 'production department', 'yes')
monitor = CopyMachine('Acer', 8, 'accounting department', 'no')
printer2 = Printer('HP', 'one', 'accounting department', 'yes')
store.add_to_store(scanner)
store.add_to_store(printer1)
store.add_to_store(monitor)
store.show_dict()
store.remover(1)
store.show_dict()
