from my_service.srv import AddTwoIntSrv
from my_service.srv import AddTwoIntSrvResponse
import time
import rospy
#-----------------------------------------------#
def handle_add_two_ints(req):
    print(f"Returning {req.a} + {req.b} = {req.a + req.b}")
    time.sleep(5)
    sum_response = AddTwoIntSrvResponse(req.a + req.b)
    return sum_response

def add_two_ints_server():
    rospy.init_node('add_two_ints_server')
    s = rospy.Service('add_two_ints', AddTwoIntSrv, handle_add_two_ints)
    print('Ready to add Two Ints...')
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()
    