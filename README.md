# ROS-For-Beginners

## 1. Instalación de ROS Noetic

Añadir el repositorio a la lista.

```
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
```

Configurar las claves.
```
sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
```

Instalación de la versión completa.
```
sudo apt-get update
sudo apt install ros-noetic-desktop-full
```

Configurar el entorno.
```
echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

[Referencia](http://wiki.ros.org/noetic/Installation/Ubuntu)

# 2. Estructura ROS

ROS está compuesto de usa serie de elementos que configuran la 

## 2.1 Paquetes

Un paquete puede incluir multipes nodos.

## 2.2 Nodos

Un nodo puede intanciarse multiples veces.

## 2.3 ROS-Topics

La entidad topic o tema en un entorno ROS es un sistema intermedio entre nodos publicadores y nodos subscriptores. Por lo tanto, es un bus dedicado al intercambio de mensajes.

Muchos a muchos


# 2. Creación de un paquete en ROS.

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

Imprimir lista de topics
```
rostopic list
```

Imprimir mensajes de un publicador a un tema
```
rostopic echo /robot_news_radio
```

Imprimir información sobre un topic
```
rostopic info /robot_news_radio
```

Publicar para debug cada 5 hercios
```
rostopic pub -r 5 /robot_news_radio std_msgs/String "data: 'Hola que tal'"
```

Debug servicio (tabular)
```
rosservice call /nombre parametros