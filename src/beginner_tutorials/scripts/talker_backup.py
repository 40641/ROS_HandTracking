#!/usr/bin/env python3
    # license removed for brevity
import rospy
from std_msgs.msg import String, Float64MultiArray

from HandTracking_IO import main

    
def talker():
        pub = rospy.Publisher('chatter', String, queue_size=10)
        rospy.init_node('talker', anonymous=True)
        rate = rospy.Rate(10) # 10hz
        while not rospy.is_shutdown():
           hello_str = "valami %s" % rospy.get_time()
           cord = str(main())
           rospy.loginfo(cord)
           pub.publish(cord)
           rate.sleep()
   
if __name__ == '__main__':
       try:
           talker()
       except rospy.ROSInterruptException:
           pass