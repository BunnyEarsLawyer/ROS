author: BunnyEarsLawyer 
date:   2/9/2017

----------------
---Basic ROS----
----------------
How to build
$ catkin_make

How to check the package got recognized
$ roscd my_package            

//
// If it doesn't work you need to source setup.bash from devel
//
$ source ./catkin_ws/devel/setup.bash

How to create a package
$ cd ./src
$ catkin_create_pkg my_package_name rospy roscpp 

How to run a node in a package
$ roscore
$ rosrun my_package my_node

How to list things
$ rospack list  
$ rosnode list  
$ rosmsg list

How to view environment variables 
$ printenv | grep ROS
$ echo $ROS_PACKAGE_PATH

----------------
---KHAN---------
----------------

2/16/2017
Summary: 
Added scripts quadrature and sample demo to CMakeLists.txt
After a 'catkin_make' they showed up after a tab completion.

$ rosrun beginner_tutorials talker.py
$ rosrun khan_control quadrature.py
$ rosrun khan_control first_demo.py 

All launch files do not work:
$ roslaunch khan_launch khan_gazebo.launch  //Use tab complete to try others









































