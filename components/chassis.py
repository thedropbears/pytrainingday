import rev
import navx
from wpimath import kinematics
from wpimath.kinematics import ChassisSpeeds
from wpimath.geometry import Rotation2d, Pose2d
from ids import Ids
from magicbot import tunable, feedback

class Chassis:
    # test of tunable
    speed_scale = tunable(0.5)

    def setup(self):
        self.drive_left  = rev.CANSparkMax(Ids.Chassis.drive_left , rev.CANSparkMax.MotorType.kBrushless)
        self.drive_right = rev.CANSparkMax(Ids.Chassis.drive_right, rev.CANSparkMax.MotorType.kBrushless)

        self.gyro = navx.AHRS.create_spi()

        self.kinematics = kinematics.DifferentialDriveKinematics(0.7)
        self.desired_chassis_speed = ChassisSpeeds(0, 0, 0)

    def drive(self, x, omega):
        self.desired_chassis_speed = ChassisSpeeds(x, 0, omega)

    def execute(self):
        wheel_speeds = self.kinematics.toWheelSpeeds(self.desired_chassis_speed)
        self.drive_left.set(wheel_speeds.left * self.speed_scale)
        self.drive_right.set(wheel_speeds.right * self.speed_scale)

    # test of feedback
    @feedback
    def getLeftSpeed(self):
        return self.drive_left.get()

    @feedback
    def getRightSpeed(self):
        return self.drive_right.get()


    def getHeading(self) -> Rotation2d:
        return self.gyro.getRotation2d()