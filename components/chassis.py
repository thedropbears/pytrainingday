from wpimath.kinematics import ChassisSpeeds
from wpimath.geometry import Rotation2d
from magicbot import will_reset_to
from math import sin, cos
import navx
import ctre

class Chassis:
    desired_velocities = will_reset_to(ChassisSpeeds(0, 0, 0))
    imu: navx.AHRS
    motor1: ctre.TalonSRX
    motor2: ctre.TalonSRX
    motor3: ctre.TalonSRX

    def __init__(self):
        # create gyro and motor objects
        self.motor1 = ctre.TalonSRX(1)
        self.motor2 = ctre.TalonSRX(2)
        self.motor3 = ctre.TalonSRX(3)

        self.imu = navx.AHRS.create_spi()
        
        # distance between center of mass and motors
        self.r = 0.5
    
    def setup(self):
        self.imu.zeroYaw()
    
    # drive reletive to the robot coordinate system
    def drive_local(self, vx, vy, omega):
        self.desired_velocities = ChassisSpeeds(vx, vy, omega)
    
    # drive reletive to the field coordinate system
    def drive_field(self, vx, vy, omega):
        self.desired_velocities = ChassisSpeeds.fromFieldRelativeSpeeds(vx, vy, omega, self.get_rotation())
    
    def execute(self):
        vx, vy, omega = self.desired_velocities.vx, self.desired_velocities.vy, self.desired_velocities.omega
        self.motor1.set(ctre.ControlMode.Velocity, vx * cos(30) - vy * cos(30) - self.r * omega)
        self.motor2.set(ctre.ControlMode.Velocity, -vx * cos(30) - vy * cos(30) - self.r * omega)
        self.motor3.set(ctre.ControlMode.Velocity, vy - self.r * omega)
    
    def get_rotation(self) -> Rotation2d:
        return self.imu.getRotation2d()