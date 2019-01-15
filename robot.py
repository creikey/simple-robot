import wpilib
import wpilib.drive
import ctre

LEFT_SLAVE_MOTOR_ID = 1
LEFT_MASTER_MOTOR_ID = 3
RIGHT_SLAVE_MOTOR_ID = 5
RIGHT_MASTER_MOTOR_ID = 2

MAIN_JOYSTICK_ID = 0


class Robot(wpilib.TimedRobot):
    def robotInit(self):
        self.left_slave_motor = ctre.WPI_TalonSRX(LEFT_SLAVE_MOTOR_ID)
        self.left_master_motor = ctre.WPI_TalonSRX(LEFT_MASTER_MOTOR_ID)
        self.right_slave_motor = ctre.WPI_TalonSRX(RIGHT_SLAVE_MOTOR_ID)
        self.right_master_motor = ctre.WPI_TalonSRX(RIGHT_MASTER_MOTOR_ID)

        self.left_slave_motor.follow(self.left_master_motor)
        self.right_slave_motor.follow(self.right_master_motor)

        self.drive = wpilib.drive.DifferentialDrive(
            self.left_master_motor, self.right_master_motor)
        self.stick = wpilib.Joystick(MAIN_JOYSTICK_ID)

    def teleopPeriodic(self):
        self.drive.arcadeDrive(self.stick.getX(), self.stick.getY())

if __name__ == '__main__':
    wpilib.run(Robot)