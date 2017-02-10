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
$ souce ./catkin_ws/devel/setup.bash

How to create a package
$ cd ./src
$ catkin_create_pkg my_package_name rospy roscpp 

How to run a node in a package
$ roscore
$ rosrun my_package my_node

How to list things
$ rospack list  
