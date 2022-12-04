#!/usr/bin/env python3

import magicbot
import wpilib
from components.chassis import Chassis
from controllers.movement import Movement

class MyRobot(magicbot.MagicRobot):
    # controllers
    movement: Movement
    # components
    chassis: Chassis

    def createObjects(self) -> None:
        # create xbox controller
        print("hello world")
        ...
    
    def teleopPeriodic(self) -> None:
        # read controller values and give them to movement
        ...
        

if __name__ == "__main__":
    wpilib.run(MyRobot)
