#!/usr/bin/env python3
import rospy 
from std_msgs.msg import Float32 

def pub () : 
    rospy.init_node("counter_node ") 
    pub = rospy.Publisher("counter_node_topic", Float32 , queue_size=2) 
    message = Float32 
    message.data = 20  
    while message.data <= 120:  
        pub.publish(message)
        rospy.loginfo(f"str{message.data}") 
        rospy.sleep(0)
        message.data += 1 
        
if __name__ == "__main__"  : 
      try :  
       pub() 
      except : 
        print('error in node counter')
    

