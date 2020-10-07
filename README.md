# ROS-For-Beginners

Creación de un paquete en ROS.

```bash
mkdir pkgname
cd pkgname
mkdir src
cd src
catkin_create_pkg my_robot_tutorials std_msgs rospy roscpp
cd ..
catkin_make
```

Añadir fichero c++

1. Editar dentro de my_robot_tutorials.

Añadir fichero python

chmod 744 my_first_node.py

 #!/usr/bin/env python3
chmod 744 my_first_node.py


Para visualización gráfica de nodos:
rosrun rqt_graph rqt_graph

Instalación del paquete turtlesim
sudo apt-get install ros-noetic-turtlesim

nano ~/.bashrc

source /opt/ros/noetic/setup.bash
source ~/Documentos/ROS-For-Beginners/devel/setup.bash

Para inicial el nucleo ROS:
```
roscore
```

## ROS-Topics

