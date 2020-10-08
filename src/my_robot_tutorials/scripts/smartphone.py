#!/usr/bin/env python3
# Título: Primer subscriptor
# Descripción: Nodo que recibe un texto por un topic indefinidamente.
# Autor: Ernesto Martínez del Pino

import rospy
from std_msgs.msg import String

def radio_data(msg):
    rospy.loginfo("Mensaje: ")
    rospy.loginfo(msg)

if __name__ == "__main__":
    rospy.init_node('smartphone')

    sub = rospy.Subscriber("/robot_news_radio", String, callback = radio_data)

    # Parar el script hasta que el nodo muera
    rospy.spin()