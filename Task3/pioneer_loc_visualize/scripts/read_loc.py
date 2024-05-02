import rospy
from geometry_msgs.msg import Pose2D
import matplotlib.pyplot as plt
import numpy as np
import time

def get_robot_pose(data):
    rospy.loginfo("I heard: {}".format(data.theta*(180/np.pi)))
    plt.axis('equal')
    plt.plot(data.x,data.y,marker=(3,0,data.theta*(180/np.pi)-90), markersize=20, color='green')
    plt.draw()
    plt.pause(0.01)


def listener():
    rospy.init_node('pioneer_control',anonymous=True)
    rospy.Subscriber('/pioneer_loc',Pose2D,get_robot_pose)
    rospy.spin()
if __name__ == '__main__':
    listener()