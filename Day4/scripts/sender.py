#! /usr/bin/env python

import rospy 
from Day4.msg import Num

rospy.init_node('sender') 
pub = rospy.Publisher('/Num', Num, queue_size=1) 
rate = rospy.Rate(1) 
Num = Num() 
while not rospy.is_shutdown():
  Num.realnum = input("enter integer part")
  Num.imaginarynum = input("enter complex part")
  rospy.loginfo(Num)
  pub.publish(Num)
  rate.sleep()