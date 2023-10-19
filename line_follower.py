#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.robotics import DriveBase

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

line_sensor = ColorSensor(Port.S4)

robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

BLACK = 9
WHITE = 85
threshold = (BLACK + WHITE) / 2

DRIVE_SPEED = 50
PROPORTIONAL_GAIN = 1.1

while True:
    deviation = line_sensor.reflection() - threshold

    turn_rateR = PROPORTIONAL_GAIN * deviation
    turn_rateL = -PROPORTIONAL_GAIN * deviation

    robot.drive(DRIVE_SPEED, turn_rateR)
    robot.drive(DRIVE_SPEED, turn_rateL)

    wait(10)