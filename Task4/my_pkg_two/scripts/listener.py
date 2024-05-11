import rospy
from std_msgs.msg import String


def callback(data: String):
    # this function receives the message and prints the content in
    # the loginfo
    rospy.loginfo(rospy.get_caller_id()+"I heard {}".format(data.data))

def listener():
    # initializing the node with unique id
    rospy.init_node('listener', anonymous=True)
    # creating a subscriber to the topic "chatter" with String data type
    # and when it receives any message it calls the function callback
    rospy.Subscriber('chatter', String, callback=callback)
    # spin function's functionality is to hold the node until its 
    # shutdown
    rospy.spin()


if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInternalException:
        pass
