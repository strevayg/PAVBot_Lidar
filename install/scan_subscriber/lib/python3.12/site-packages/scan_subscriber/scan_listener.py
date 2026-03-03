import rclpy
import math
from rclpy.node import Node
from sensor_msgs.msg import LaserScan

class ScanListener(Node):
    def __init__(self):
        super().__init__('scan_listener')
        self.subscription = self.create_subscription(LaserScan, '/scan', self.scan_callback, 10)
    def indexCalculator(self,msg,angle):
        index = int((angle - msg.angle_min) / msg.angle_increment)
        index %= len(msg.ranges) # properly wraps around 
        return index 
    def scan_callback(self, msg):
        # whatever we want it to do! test this rn with some prints
        # this will give the front index 
        # (directly in front where the arrow and logo RPLIDAR is)
        # angle_min = -pi    | angle_max = pi    | angle_increment = .00196 rad (.1125deg)
        # for ros2 0rad is pointing at the wires 
        leftIndex = self.indexCalculator(msg, (3*math.pi)/2)
        leftDist = msg.ranges[leftIndex]
        self.get_logger().info(f"Left Distance: {leftDist:.2f} m")
        frontIndex = self.indexCalculator(msg, math.pi) #rads (everything is in rads)
        frontDist = msg.ranges[frontIndex]
        self.get_logger().info(f"Front distance: {frontDist:.2f} m")
        rightIndex = self.indexCalculator(msg, math.pi/2) # physical right
        rightDist = msg.ranges[rightIndex]
        self.get_logger().info(f"Right distance: {rightDist:.2f} m")

def main():

    rclpy.init()
    node = ScanListener()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
