#!/usr/bin/python3
#Author: Bhavesh Jain
import rospy
from std_msgs.msg import String
from std_msgs.msg import Int64
from std_msgs.msg import Time
import time

#Publisher function to publish second data to node i.e topic 2
class Publisher:
	"""
	This Class is meant to explain Publishers in ROS.
	 __init__(self) of a class is the first function that runs of the class
	 when the class is initialized.
	 self is a default member of a class that can store any object.
	Publishers are any nodes in the system that publishes a specific message
	over a specific topic.
	"""
	def __init__(self, topic_name, publish_rate, type, message):
		print("Initializing Node")
		#Initializes the Node.
		if type == "String":
			data_type = String
		elif type == "Int64":
			data_type = Int64
		elif type == "Time":
			data_type = Time

		rospy.init_node("publisher_node")
		#Initializes a publisher within the node
		
		self.publisher = rospy.Publisher(topic_name, data_type, queue_size=10)
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
		self.message = data_type(message)
		

	def timerCallback(self, event):
		print("Publishing message: ", self.message.data)
		self.publisher.publish(self.message)

if __name__ == '__main__':

	p = Publisher("topic1", 1,"String", "Text Message")
	p = Publisher("topic2", 1,"Int64",12345)
	p = Publisher("topic3", 1,"Time",rospy.get_rostime())
	rospy.spin()