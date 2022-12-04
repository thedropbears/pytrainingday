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
        self.gamepad = wpilib.XboxController(0)
    
    def teleopPeriodic(self) -> None:
        # read controller values and give them to movement
        x_input = -self.gamepad.getLeftY()
        y_input = -self.gamepad.getLeftX()
        omega = -self.gamepad.getRightX()
        a_input = self.gamepad.getAButton()
        self.movement.set_inputs(x_input, y_input, omega, a_input)
        

if __name__ == "__main__":
    wpilib.run(MyRobot)
