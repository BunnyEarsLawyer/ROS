author: BunnyEarsLawyer
date:   2/9/2017

$ roscd my_khan_package //source devel setup.bash if this does not work

What are each of the folders?
src
- khan_control     = package that has nodes to control khan
- khan_launch      = helpful files that launch nodes for me, including roscore
- khan_msgs        = nodes pass each other messages, these are defined here for convenience
- khan_description = this places has the models used to use the robot in simulation (gazebo)

date: 2/9/2017
I 'made' ros nodes out of the sample python files like in beginner_tutorials
$ src/khan_control/scripts
$ chmod +x quadrature.py


How to launch rviz
