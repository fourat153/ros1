#!/usr/bin/env python3
import rospy 
from geometry_msgs.msg import Twist 

def pub () : 
    rospy.init_node("node_tur") 
    pub = rospy.Publisher("turtle1/cmd_vel", Twist , queue_size=2) 
    message = Twist()
    message.angular.z = 0.5 
    message.linear.x = 0.5
    while not rospy.is_shutdown() :
        pub.publish(message)
        rospy.loginfo(f"str{message.angular.z} , str{message.linear.x}") 
        rospy.sleep(0)
if __name__ == "__main__"  : 
      try :  
       pub() 
      except : 
        print('error in node counter')