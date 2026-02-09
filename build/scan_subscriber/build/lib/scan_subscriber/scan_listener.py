import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan

class ScanListener(Node):
    def __init__(self):
        super().__init__('scan_listener')
        self.subscription = self.create_subscription(LaserScan, '/scan', self.scan_callback, 10)
    def scan_callback(self, msg):
        # whatever we want it to do! test this rn with some prints idk
        centerIndex = len(msg.ranges)//2 #floor divide to get the index @ front
        frontDist = msg.ranges[centerIndex]
        self.get_logger().info(f"Front distance: {frontDist:.2f} m")

def main():
    rclpy.init()
    node = ScanListener()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
