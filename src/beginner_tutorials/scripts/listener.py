#!/usr/bin/env python3
import rospy
from std_msgs.msg import String, Float64MultiArray, Float64
from HandTracking_IO import *

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    
def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("chatter", Float64MultiArray, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()
