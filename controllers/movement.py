from magicbot import StateMachine, state, timed_state, default_state
from components.chassis import Chassis
from wpimath.controller import ProfiledPIDController
from wpimath.trajectory import TrapezoidProfile
import math

class Movement(StateMachine):
    chassis: Chassis

    def setup(self):
        self.heading_pid = ProfiledPIDController(1, 0, 0.2, TrapezoidProfile.Constraints(3, 3))
        self.heading_pid.setGoal(math.pi/2)

        self.input_x = 0
        self.input_omega = 0

    def set_inputs(self, x, omega):
        self.input_x = x
        self.input_omega = omega

    def set_autoalign(self, value):
        if value:
            self.engage()
        else:
            self.done()

    @default_state
    def normal_drive(self):
        self.chassis.drive(self.input_x, self.input_omega)

    @state(first=True)
    def align_heading(self, initial_call):
        cur_heading = self.chassis.getHeading().radians()
        if initial_call:
            self.heading_pid.reset(cur_heading)

        pid_output = self.heading_pid.calculate(cur_heading)
        self.chassis.drive(self.input_x, pid_output)