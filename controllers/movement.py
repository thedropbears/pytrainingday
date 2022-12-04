import magicbot
from components.chassis import Chassis
import navx

class Movement:
    chassis: Chassis
    set_point = magicbot.tunable(0)
    Kd = magicbot.tunable(0)
    Kp = magicbot.tunable(0)

    def __init__(self):
        self.last_error = self.chassis.get_rotation().radians()-self.set_point

    # take commanded speeds    
    def set_inputs(self, vx, vy, omega):
        ...
    
    def set_autoalign(self, value):
        ...
    
    def set_field_oriented(self, value):
        ...
    
    def execute(self):
        # if autoalign compute rotation pid
        # tell the chassis to drive
        error = self.chassis.get_rotation().radians()-self.set_point
        P = error*self.Kp
        D = self.last_error-error
        controller_output = P + D
        self.last_error = error
        self.chassis.drive_field(0, 0, controller_output)