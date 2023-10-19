#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.robotics import DriveBase


obstacle_sensor = UltrasonicSensor(Port.S1)

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)


def avoid():
    robot.straight(-20)
    robot.turn(90)

    robot.straight(300)
    robot.turn(-90)
    robot.straight(500)
    robot.turn(-90)
    robot.straight(550)
    robot.turn(-90)
    robot.straight(520)
    robot.turn(-90)
    robot.straight(400)
    robot.turn(90)
    

while True:
    robot.drive(200, 0)   
    while obstacle_sensor.distance() >150:
        wait(10)
    distance = robot.distance()
    avoid()
    robot.straight(distance)

    break
    

