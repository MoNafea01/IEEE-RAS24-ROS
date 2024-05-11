import rospy
from std_msgs.msg import String


def talker():
    # creating publisher to the topic "chatter" with String type, and size of 
    # the buffer to save the messages is 10 messages
    pub = rospy.Publisher('chatter',String,queue_size=10)
    car_pub = rospy.Publisher('car_channel',String,queue_size=10)
    # initialize the node with  unique id(anonymous)
    rospy.init_node('talker',anonymous=True)
    # frequency = 10 hz (10 messages every second) so the buffer will 
    # reset every second
    rate = rospy.Rate(5)
    # while the user didn't shutdown the program do the following instructions
    while not rospy.is_shutdown():
        # hello world + time
        hello_str = "hello world {}".format(rospy.get_time())
        # printing the hello message
        #rospy.loginfo(hello_str)
        # publish the message
        pub.publish(hello_str)
        # sleep function here is used to apply the delay between each message and
        # others
        rate.sleep()
    

if __name__ == '__main__':
    try:
        #global freq
        #freq = rospy.get_param("freq")
        talker()
    except rospy.ROSInternalException:
        pass