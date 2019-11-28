class Robot:
    """
    This is the definition of a robot with a name, energy, or compound
    that attacks other robots and unite with another robot
    to become a compound robot
    """
    def __init__(self, name=None, energy=20, compound=None):
        """
        Initialize the name, energy level, and compound robot instance
        for this robot if there are any passed arguments
        """
        self.name = name
        self.energy = energy
        self.compound = compound

    def __add__(self, other):
        """
        Add this robot to another to create a CompoundRobot object
        and set compound robot reference to both robots
        Args:
            (Robot obj): Another robot to be combined with this one
        Returns:
            (CompoundRobot obj): Combined robots into one compound robot
        """
        # Create compound robot
        compound_robot = CompoundRobot(self, other)
        # Set compound robot reference to this robot
        self.compound = compound_robot
        # Set compound robot reference to the other robot
        other.compound = compound_robot
        # Return compound robot
        return compound_robot

    def attack(self, other, energy):
        """
        Robots attack each other with a given energy
        - Whichever robot has the highest energy
            takes the given energy from the other
        - If the other has less energy than the given one,
            the winning robot only takes the amount of the losing robot - 1
        - If the robots have the same energy,
            the attacking robot loses the given energy
            and the attacked robot remains the same
        Args:
            (Robot obj): Another robot to battle against
            (integer): Amount of energy taken away
        """

        # This robot may lose the given energy or all its energy - 1
        lose_self = self.energy - 1 if self.energy < energy else energy
        # The other robot may lose the given energy or all its energy - 1
        lose_other = other.energy - 1 if other.energy < energy else energy

        # Check if this robot has the greater energy
        if self.energy > other.energy:
            # This robot gets energy points from the other robot
            self.energy += lose_other
            other.energy -= lose_other
        # Check if the other robot has the greater energy
        elif self.energy < other.energy:
            # The other robot gets energy points from this robot
            other.energy += lose_self
            self.energy -= lose_self
        # Check if both robots have the same energy
        else:
            # Only this robot loses given energy
            self.energy -= energy


class CompoundRobot(Robot):
    """
    This is the definition of a compound robot
    with initial two robots that can receive more robots
    as well as attack other robots like a simple robot
    """
    def __init__(self, robot1, robot2):
        """
        Initialize the components and energy of this compound robots
        with two robots and their energy points
        """
        super().__init__()
        self.components = [robot1, robot2]
        self.energy = robot1.energy + robot2.energy

    def __iadd__(self, other):
        """
        Add this robot to this compound robot
        and set compound robot reference of additional robot
        to this compound robot
        Args:
            (Robot obj): Another robot to be combined with
                this compound robot
        Returns:
            (CompoundRobot obj): This compound robot with additional robot
        """
        # Add robot to compound robot components
        self.components.append(other)
        # Add energy level
        self.energy += other.energy
        # Set compound robot reference to the other robot
        other.compound = self
        return self
