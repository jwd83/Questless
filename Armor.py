class Armor:

    armor_physical = 1
    armor_magical = 1

    name = 'cloth armor'
    type = 'chest'

    def __init__(self, armor_physical = 1, armor_magical = 1, name='cloth armor', type='chest'):
        self.armor_physical = armor_physical
        self.armor_magical = armor_magical
        self.name = name
        self.type = type

    def __str__(self):
        return '{}: {}'.format(self.type, self.name)
