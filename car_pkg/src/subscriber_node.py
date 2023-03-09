#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64


def front_left_steering_callback(msg):
    angle = msg.data
    print("Received left angle: " + str(angle))


def front_right_steering_callback(msg):
    angle = msg.data
    print("Received right angle: " + str(angle))


def front_left_throttle_callback(msg):
    throttle = msg.data
    print("Received left throttle: " + str(throttle))


def front_right_throttle_callback(msg):
    throttle = msg.data
    print("Received right throttle: " + str(throttle))

if __name__ == '__main__': 

    sub_right = rospy.Subscriber('/car_controller/front_right_steering/command', Float64, front_left_steering_callback, queue_size=1)
    sub_left = rospy.Subscriber('/car_controller/front_left_steering/command', Float64, front_right_steering_callback, queue_size=1)
    sub_move = rospy.Subscriber('/car_controller/rear_controller/command', Float64, front_left_throttle_callback, queue_size=1)
    rospy.init_node("subscriber_node")
    print("Started subscriber node")
    rospy.spin()