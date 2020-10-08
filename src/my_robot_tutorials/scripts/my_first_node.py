#!/usr/bin/env python3
# Título: Primer nodo
# Descripción: nodo que imprime el mismo mensaje indefinidamente.
# Autor: Ernesto Martínez del Pino

import rospy

if __name__ == "__main__":
    # Nombre del nodo debe ser único entre los nodos
    # Debe ser diferente del nombre del fichero
    rospy.init_node('my_first_python_node')
    # Imprimir mensaje por pantalla
    rospy.loginfo('This node has been started')

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        rospy.loginfo("Hola")
        rate.sleep()