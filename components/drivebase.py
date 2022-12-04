import ctre
from math import sin, cos

class Drivebase : 
    def __init__(self):
        self.motor1 = ctre.TalonSRX(1)
        self.motor2 = ctre.TalonSRX(2)
        self.motor3 = ctre.TalonSRX(3)

        # dist from center to wheel
        self.r = 0.5 # meters

    def to_wheel_speeds(self, Vx, Vy,W):
        motor1 = sin(-30) * Vx + cos(-30)*Vy + W/self.r
        motor2 = Vy + W/self.r
        motor3 = sin(30) * Vx + cos(30) * Vy + W/self.r
        return motor1, motor2, motor3

    
    




        