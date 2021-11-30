#!/usr/bin/python3
#Author: Bhavesh Jain
import rospy
from std_msgs.msg import Float64

class Publisher:
	def __init__(self, topic_name, publish_rate, message):
		print("Initializing Node")
		#Initializes the Node.

		rospy.init_node("publisher_node")
		#Initializes a publisher within the node
		
		self.publisher = rospy.Publisher(topic_name, Float64, queue_size=10)
		#Initializing a timer

		period = rospy.Duration(publish_rate)

		# This timer runs timerCallback() func once every second
		self.timer = rospy.Timer(period, self.timerCallback)

		# Message to published
		self.message = Float64(message)
		

	def timerCallback(self, event):
		print("Publishing message: ", self.message.data)
		self.publisher.publish(self.message)

if __name__ == '__main__':

	p = Publisher("X", 1,	0.6)
	p = Publisher("Y", 1,	2.5)
	p = Publisher("Z", 1,	1.4)
	rospy.spin()