#!/usr/bin/env python3


import rospy
from std_msgs.msg import String
class SendingNode:
    def __init__(self):
        rospy.init_node("sending_node",anonymous=True)
        self.pub=rospy.Publisher("commandtopic",String,queue_size=10)
    def send(self,command):
        self.pub.publish(command)
        rospy.loginfo(f"sending command {command}")
    def run(self):
        rospy.loginfo("sending node is running")
        while not rospy.is_shutdown():
            command=input("Please enter command (eg : Direction Magnitude) Kindly give gap between :")
            ##directions are forward, backward , right, left 
            self.send(command)
            rospy.sleep(1)

if __name__=="__main__":
    node=SendingNode()
    node.run()
