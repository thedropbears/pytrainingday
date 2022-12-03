from magicbot import will_reset_to
from components.chassis import Chassis

class Movement:
    chassis: Chassis

    def __init__(self):
        ...

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
        ...
