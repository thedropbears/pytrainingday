#!/usr/bin/env python3

import magicbot
import wpilib
from components.chassis import Chassis
from controllers.movement import Movement
from ids import check_ids

check_ids()

class MyRobot(magicbot.MagicRobot):
    chassis: Chassis
    movement: Movement

    def createObjects(self) -> None:
        self.gamepad = wpilib.XboxController(0)

    def teleopPeriodic(self):
        vx = self.gamepad.getLeftY()
        vz = self.gamepad.getRightX()
        self.movement.set_inputs(vx, vz)
        self.movement.set_autoalign(self.gamepad.getAButton())

if __name__ == "__main__":
    wpilib.run(MyRobot)
