import rospy 
import cv2

from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

import sys
bridge = CvBridge() # creating a bridge to convert images from ros image to cv mat and vice versa
def image_callback(ros_img: Image):
    print('got image')
    global bridge
    try:
        cv_img = bridge.imgmsg_to_cv2(ros_img,'bgr8')
    except CvBridgeError as e:
        print(e)
    cv2.imshow('image_window_original',cv_img)
    cv2.waitKey(3)
    edge_img = cv2.Canny(cv_img,100,200)
    edge_ros_img = bridge.cv2_to_imgmsg(edge_img)
    cv2.imshow('image_window_with_edge',edge_ros_img)
    img_pub.publish(edge_ros_img)
def main(args):
    rospy.init_node('image_converter',anonymous=True)
    img_sub = rospy.Subscriber('/usb_cam/image_raw',Image,image_callback)
    global img_pub
    img_pub = rospy.Publisher('/canny_image',Image,queue_size=10)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print('Shutting down')
        cv2.destroyAllWindows()
if __name__ == '__main__':
    main(sys.argv)
