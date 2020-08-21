#!/usr/bin/env python 
import rospy
from std_msgs.msg import String    
def talker():
    count = 0
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
       count = count + 1
       rospy.loginfo(str(count))
       pub.publish(str(count))
       rate.sleep()
if __name__ == '__main__':
    try:
       talker()
    except rospy.ROSInterruptException:
       pass
