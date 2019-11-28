from battle_unit import Robot, CompoundRobot

if __name__ == '__main__':
    # Create three robots
    robot1 = Robot('robot1')
    robot2 = Robot('robot2')
    robot3 = Robot('robot3')
    # Display robot1's energy
    print('Robot 1 energy:', robot1.energy)

    # Create a compound robot with robot1 and robot2
    compound_robot = robot1 + robot2
    # Display compound robot's energy
    print(compound_robot.energy)

    # Add robot3 into the compound robot
    compound_robot += robot3
    # Display additional energy
    print(compound_robot.energy)
