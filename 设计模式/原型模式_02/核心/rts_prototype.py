from prototype_1 import Prototype
from copy import deepcopy


class Knight(Prototype):
    def __init__(self, level):
        self.unit_type = 'Knight'

        filename = f'{self.unit_type}_{level}.dat'

        with open(filename, 'r') as parameter_file:
            lines = parameter_file.read().split('\n')
            self.life = lines[0]
            self.speed = lines[1]
            self.attack_power = lines[2]
            self.attack_range = lines[3]
            self.weapon = lines[4]

    def __str__(self):
        return f'Type: {self.unit_type}\n' \
               f'Speed: {self.life}\n' \
               f'Attack Power: {self.speed}\n' \
               f'Attack Range: {self.attack_power}\n' \
               f'Weapon: {self.attack_range}\n'

    def clone(self):
        return deepcopy(self)


class Archer(Prototype):
    def __init__(self, level):
        self.unit_type = 'Archer'

        filename = f'{self.unit_type}_{level}.dat'

        with open(filename, 'r') as parameter_file:
            lines = parameter_file.read().split('\n')
            self.life = lines[0]
            self.speed = lines[1]
            self.attack_power = lines[2]
            self.attack_range = lines[3]
            self.weapon = lines[4]

    def __str__(self):
        return f'Type: {self.unit_type}\n' \
               f'Life: {self.life}' \
               f'Speed: {self.speed}\n' \
               f'Attack Power: {self.attack_power}\n' \
               f'Attack Range: {self.attack_range}' \
               f'Weapon: {self.weapon}'

    def clone(self):
        return deepcopy(self)


class Barracks(object):
    def __init__(self):
        self.units = {
            'knight': {
                1: Knight(1),
                2: Knight(2)
            },
            'archer': {
                1: Archer(1),
                2: Archer(2)
            }
        }

    def build_unit(self, unit_type, level):
        return self.units[unit_type][level].clone()


if __name__ == '__main__':
    barracks = Barracks()
    knight1 = barracks.build_unit('knight', 1)
    archer1 = barracks.build_unit('archer', 2)
    print(f'[knight1] {knight1}')
    print(f'[archer1] {archer1}')
