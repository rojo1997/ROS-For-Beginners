#!/usr/bin/env python3
# Título: Primer publicador
# Descripción: Nodo que publica a un topic el mismo mensaje indefinidamente.
# Autor: Ernesto Martínez del Pino

import rospy
from std_msgs.msg import String

if __name__ == "__main__":
    rospy.init_node('robot_news_radio_transmitter', anonymous = True)

    pub = rospy.Publisher(
        "/robot_news_radio", 
        String, 
        queue_size = 10
    )

    rate = rospy.Rate(2)

    # Necesario introducir la condición ya que nodo termina pero
    # el script no.
    while not rospy.is_shutdown():
        msg = String()
        msg.data = "Hola que tal"
        pub.publish(msg)
        rate.sleep()

    rospy.loginfo("Node was stopped")