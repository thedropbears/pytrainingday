import magicbot
from components.chassis import Chassis
import navx

class Movement:
    chassis: Chassis
    set_point = magicbot.tunable(0)
    Kp = magicbot.tunable(0)
    Kd = magicbot.tunable(0)

    def setup(self):
        self.input_x = 0
        self.input_y = 0
        self.input_omega = 0
        self.last_error = self.chassis.get_rotation().radians()-self.set_point

    # take commanded speeds    
    def set_inputs(self, vx, vy, omega, a_button):
        self.input_x = vx
        self.input_y = vy
        self.input_omega = omega
        self.input_a = a_button
    
    def execute(self):
        # if autoalign compute rotation pid
        # tell the chassis to drive
        error = self.chassis.get_rotation().radians()-self.set_point
        P = error*self.Kp
        D = (self.last_error-error) * self.Kd
        controller_output = P + D
        self.last_error = error
        if self.input_a:
            self.chassis.drive_field(self.input_x, self.input_y, controller_output)
        else:
            self.chassis.drive_field(self.input_x, self.input_y, self.input_omega)