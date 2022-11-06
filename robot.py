#!/usr/bin/env python3

import magicbot
import wpilib

class MyRobot(magicbot.MagicRobot):
    def createObjects(self) -> None:
        pass

if __name__ == "__main__":
    wpilib.run(MyRobot)
