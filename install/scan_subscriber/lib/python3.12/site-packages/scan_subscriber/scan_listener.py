import rclpy
from math import sin
from rclpy.node import Node
from numpy import linspace, inf
from sensor_msgs.msg import LaserScan

class ScanListener(Node):
    def __init__(self):
        super().__init__('scan_listener')
        self.publisher = self.create_publisher(LaserScan, '/flitered_scan', 10)
        self.subscription = self.create_subscription(LaserScan, '/scan', self.scan_callback, 10)
        
        self.width = .73152  # width of pavbot (m) assuming 2.4ft
        self.extent = self.width / 2.0 # center to edge distance so lidar doesnt react to itself 
        self.get_logger().info('Publishing filtered_scan topic. Use Rviz for visualization.')
    def indexCalculator(self,msg,angle):
        index = int((angle - msg.angle_min) / msg.angle_increment)
        index %= len(msg.ranges) # properly wraps around 
        return index 
    def scan_callback(self, msg):
        # whatever we want it to do; return a LaserScan topic with a reduced ranges array 
        # ranges will just give the front 180 degree frame of reference for the lidar
        #    can be adjusted, change the indeces within points array

        # (directly in front where the arrow and logo RPLIDAR is)
        # angle_min = -pi    | angle_max = pi    | angle_increment = .00196 rad (.1125deg)
        # for ros2 0rad is pointing at the wires 
        # left: 3pi/2 (270)   | front: pi (180)   | right: pi/2 (90)
        angles = linspace(msg.angle_min, msg.angle_max, len(msg.ranges))
        points = [r * sin(theta) if (theta <  -1.5708 or theta > 1.5708) else inf for r, theta in zip(msg.ranges, angles)]
        newRanges = [r if abs(y) < self.extent else inf for r,y in zip(msg.ranges, points)]
        msg.ranges = newRanges
        self.publisher.publish(msg)
def main():

    rclpy.init()
    node = ScanListener()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
