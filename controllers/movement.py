from magicbot import will_reset_to
from components.chassis import Chassis
import navx

class Movement:
    chassis: Chassis

    def __init__(self):
        self.set_point = 0
        self.Kd = 0
        self.Kp = 0
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