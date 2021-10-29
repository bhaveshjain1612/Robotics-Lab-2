#!/usr/bin/python3
#Author: Bhavesh Jain
import rospy
from std_msgs.msg import String
class Publisher:
	"""
	This Class is meant to explain Publishers in ROS.
	 __init__(self) of a class is the first function that runs of the class
	 when the class is initialized.
	 self is a default member of a class that can store any object.
	Publishers are any nodes in the system that publishes a specific message
	over a specific topic.
	"""
	def __init__(self, topic_name, publish_rate):
		print("Initializing Node")
		#Initializes the Node.
		
		rospy.init_node("publisher_node")
		#Initializes a publisher within the node
		
		self.publisher = rospy.Publisher(topic_name, String, queue_size=10)
		#Initializing a timer
		"""
		A timer periodically runs a function.
		rospy.Timer(period_in_seconds, function_to_call)
		The function being called at every period is called, Callback
		"""
		period = rospy.Duration(publish_rate)

		# This timer runs timerCallback() func once every second
		self.timer = rospy.Timer(period, self.timerCallback)

		# Message to published
		self.string_message = String("Message sent")
		

	def timerCallback(self, event):
		print("Publishing message: ", self.string_message.data)
		self.publisher.publish(self.string_message)

if __name__ == '__main__':

	p = Publisher("topic1", 1)
	rospy.spin()
