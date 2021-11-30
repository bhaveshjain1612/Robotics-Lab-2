import rospy
from std_msgs.msg import Int64

msg = Int64(1234)

print(msg.data)