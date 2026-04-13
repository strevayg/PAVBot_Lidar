



# PAVBOT LIDAR ROS2 Package
ROS2 node for subscribing to /scan from SLAMTEC LIDAR scans using SLAMTEC LIDAR SLLIDAR Package for S2 Model
Submodule: https://github.com/Slamtec/sllidar_ros2
- - -
## How to Install
git clone --recurse-submodules https://github.com/strevayg/PAVBot_Lidar
- - - 
## How to Run
* Assuming ROS2 has already been installed and correctly configured with builds 
  - (check sllidar_ros2 package if unclear)
* Run with view or another file via sllidar 
  - ros2 launch sllidar_ros2 view_sllidar_s2_launch.py (view allows RViz Control Window)
  - ros2 launch sllidar_ros2 sllidar_s2_launch.py
* In another terminal launch the /scan subscriber node
  - ros2 run scan_subscriber scan_listener
  - This node filters out the back 180deg of the LiDAR scan under the topic /filtered_scan in RViZ
  - Remember: add this node to the launch file youre using as this is not included in this repo

