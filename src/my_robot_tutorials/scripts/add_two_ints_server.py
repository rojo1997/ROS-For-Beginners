#!/usr/bin/env python3
import rospy
from rospy_tutorials.srv import AddTwoInts

def handle_add_two_ints(req):
    rospy.loginfo(type(req))
    result = req.a + req.b
    rospy.loginfo("Sum: " + str(result))
    return result

if __name__ == "__main__":
    rospy.init_node('add_two_ints_server')
    rospy.loginfo('Add two ints server node created')

    # Empezar siempre con un nombre para servidores
    # Comprueba si la entrada se adapta a AddTwoInts
    service = rospy.Service(
        name = "/add_two_ints", 
        service_class = AddTwoInts,
        handler = handle_add_two_ints
    )

    rospy.loginfo("Service server has been started")
    rospy.spin()

