#!/usr/bin/env python3


import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

class Commander:
    def __init__(self):
        rospy.init_node("commander",anonymous=True)
        self.pub=rospy.Publisher("/cmd_vel",Twist,queue_size=10)
        rospy.Subscriber("commandtopic",String,self.clbk)
    def clbk (self,msg):
        self.x=msg.data.split()
        rospy.loginfo(f"COmmand received {self.x[0]} and {self.x[1]}")


        velocity=Twist()
        if  self.x[0].lower()=="forward":
            velocity.linear.x=float(self.x[1])
            velocity.linear.y=0
            velocity.linear.z=0
            velocity.angular.x=0
            velocity.angular.y=0
            velocity.angular.z=0
        elif self.x[0].lower()=="backward":
            velocity.linear.x=-float(self.x[1])
            velocity.linear.y=0
            velocity.linear.z=0
            velocity.angular.x=0
            velocity.angular.y=0
            velocity.angular.z=0
        elif self.x[0].lower()=="rightward":
            velocity.linear.x=0
            velocity.linear.y=0
            velocity.linear.z=0
            velocity.angular.x=0
            velocity.angular.y=0
            velocity.angular.z=float(self.x[1])
        elif self.x[0].lower()=="leftward":
            velocity.linear.x=0
            velocity.linear.y=0
            velocity.linear.z=0
            velocity.angular.x=0
            velocity.angular.y=0
            velocity.angular.z=-float(self.x[1])
        self.pub.publish(velocity)
    def run(self):
        rospy.spin()

if __name__=="__main__":
    node=Commander()
    node.run()
