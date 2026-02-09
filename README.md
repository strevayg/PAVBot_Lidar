



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
* Run with view or another file via sllidar (view allows RViz Control Window)
  - ros2 launch sllidar_ros2 view_sllidar_s2_launch.py
  - ros2 launch sllidar_ros2 sllidar_launch.py
* In another terminal launch the /scan subscriber node
  - ros2 run scan_subscriber scan_listener

