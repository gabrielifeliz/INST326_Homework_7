from battle_unit import Robot, CompoundRobot

if __name__ == '__main__':
    robot1 = Robot('robot1')
    robot2 = Robot('robot2')
    robot3 = Robot('robot3')
    print('Robot 1 energy:', robot1.energy)

    compound_robot = robot1 + robot2
    print(compound_robot.energy)

    compound_robot += robot3
    print(compound_robot.energy)
