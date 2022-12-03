from wpimath.kinematics import ChassisSpeeds
from wpimath.geometry import Rotation2d
from magicbot import will_reset_to
import navx
import ctre

class Chassis:
    desired_velocities = will_reset_to(ChassisSpeeds(0, 0, 0))
    def __init__(self):
        # create gyro and motor objects
        ...

    # drive reletive to the robot coordinate system
    def drive_local(self, vx, vy, omega):
        # set desired velocities
        ...
    
    # drive reletive to the field coordinate system
    def drive_field(self, vx, vy, omega):
        # set desired velocities rotated from global to local coordinate system
        # done using a rotation matrix
        # https://www.gatevidyalay.com/2d-rotation-in-computer-graphics-definition-examples/
        # ChassisSpeeds.fromFieldRelativeSpeeds() does this for us
        ...
    
    def execute(self):
        # calculate motors speeds
        # command motors
        ...
    
    def get_rotation(self) -> Rotation2d:
        # get rotation from gyro
        ...