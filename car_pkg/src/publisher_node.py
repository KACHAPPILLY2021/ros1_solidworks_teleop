#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64

if __name__ == '__main__': 

    pub_right = rospy.Publisher('/car_controller/front_right_steering/command', Float64, queue_size=1)
    pub_left = rospy.Publisher('/car_controller/front_left_steering/command', Float64, queue_size=1)
    pub_move = rospy.Publisher('/car_controller/rear_controller/command', Float64, queue_size=1)
    
    rospy.init_node("publisher_node")
    print("Started publisher node")

    rate = rospy.Rate(1) # 1hz
    
    speed = 20
    turn_angle = 0.55
    while not rospy.is_shutdown():
        print("Publishing velocity: " + str(speed) + ", angle: "  + str(turn_angle))
        pub_right.publish(turn_angle)
        pub_left.publish(-turn_angle)
        pub_move.publish(speed)
        rate.sleep()