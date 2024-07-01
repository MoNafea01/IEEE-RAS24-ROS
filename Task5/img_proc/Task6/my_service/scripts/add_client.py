import sys
import rospy
from my_service.srv import AddTwoIntSrv
#-----------------------------------------------#
def add_two_ints_client(x,y):
    rospy.wait_for_service('add_two_ints')
    try:
        add_two_ints = rospy.ServiceProxy('add_two_ints',AddTwoIntSrv)
        resp = add_two_ints(x,y)
        return resp.sum
    except rospy.ServiceException as e:
        print("Service call failed: {e}")

if __name__ == "__main__":
    if (len(sys.argv)) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        sys.exit(1)
    print(f"Requesting {x} + {y}")
    print(f"{x} + {y} = {add_two_ints_client(x,y)}")