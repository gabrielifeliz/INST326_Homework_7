class Robot:
    def __init__(self, name=None, energy=20, compound=None):
        self.name = name
        self.energy = energy
        self.compound = compound

    def __add__(self, other):
        return self

    def attack(self, other):
        self.energy += other.energy - 1
        other.energy += other.energy - 1


class CompoundRobot(Robot):
    def __init__(self, robot1, robot2):
        self.components = []
        self.energy = robot1.energy + robot2.energy

    def __iadd__(self, other):
        return self
