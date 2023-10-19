#!/usr/bin/env pybricks-micropython

from pybricks.ev3devices import Motor, UltrasonicSensor, ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.robotics import DriveBase

obstacle_sensor = UltrasonicSensor(Port.S1)

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
line_sensor = ColorSensor(Port.S3)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

BLACK = 9
WHITE = 85
DRIVE_SPEED = 150
threshold = (BLACK + WHITE) / 2

def detect_line():
    deviation = line_sensor.reflection() - threshold
    if deviation < 0:
        robot.stop()
        robot.straight(-20)
        robot.turn(-20)

while True:
    robot.straight(5)
    while obstacle_sensor.distance() < 5000:
        detect_line()
        robot.drive(DRIVE_SPEED, 0)
    else:
        robot.turn(20)
        detect_line()