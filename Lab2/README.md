# Lab 2
## Contents
### Publisher
Code for the publisher file for the lab.<br>
This file is used to publish information to the node.
### Subscriber
Code for the subscriber file for the lab.<br>
This file is used to read information from the node, that was published by the publisher.
### Launch
This is alunch file for the **pub_sub_pkg** package and can be used to launch both _publisher_ and _subscriber_ files.<br>
This file is named _pub_sub.launch_
###Note
Before launching the either of the files, execute the commands below in the terminal:<br>
#### Shift Directory to _catkin workspace_
```
cd catkin_ws/
```
#### Source the setup files
```
source devel/setup.bash
```
#### Start _ROScore_
Enter the folloeing command in a new terminal window
```
roscore
```
#### Launch the _launch_ file
Here, the name _pub_sub_pkg_ is the name of the ros package created earlier and _pub_sub.launch_ is the name of the launch file
```
roslaunch pub_sub_pkg pub_sub.launch
```
