#!/usr/bin/python3
#Author: Bhavesh Jain
import rospy
from std_msgs.msg import Int64 as count
from std_msgs.msg import String
from std_msgs.msg import Time

#Subscriber function to read data from second publisher i.e topic 2
class subscriber:
	"""
	 This class’ purpose is to demonstrate subscribers.
	"""
	"""
	 Subscribers subscribe or listen to a topic and extract information
	 from it in a predefined structure.
	"""
	def __init__(self, topic_name,type,message):

		if type == "String":
			data_type = String
		elif type == "count":
			data_type = count
		elif type == "Time":
			data_type = Time

		rospy.init_node("subscriber_node_temp")
		self.sub = rospy.Subscriber(topic_name , data_type, self.callback)
		self.message = message
	
	def callback(self, msg):
		print(self.message,msg.data)
	
if __name__ == '__main__':
	s = subscriber("topic1",'String','Text Message Read: ')
	s = subscriber("topic2","count","Integer number Read: ")
	s = subscriber("topic3","Time","Time Read: ")

	rospy.spin()