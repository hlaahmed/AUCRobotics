#!/usr/bin/env python
import rospy
from Day4.msg import Num  
def callback(Num):
   rospy.loginfo(rospy.get_caller_id() + "I heard %d + %d i",Num.realnum,Num.imaginarynum)      
def listener():
   rospy.init_node('listener', anonymous=True)   
   rospy.Subscriber("/Num", Num, callback)
   rospy.spin()
   
if __name__ == '__main__':
       listener()
