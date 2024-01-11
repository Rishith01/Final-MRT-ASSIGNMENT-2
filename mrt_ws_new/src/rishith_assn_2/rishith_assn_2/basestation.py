import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, String
from geometry_msgs.msg import Point

class BaseStationSubscriber(Node):
    def __init__(self):
        super().__init__('basestation')

        # Subscribe to topic1 (std_msgs/Float32) for altitude values
        self.subscription = self.create_subscription(
            Float32,
            'topic1',
            self.callback,
            10  # QoS profile
        )
        self.subscription  # Prevent unused variable warning

        # Subscribe to topic2 (geometry_msgs/Point) for location data
        self.subscription = self.create_subscription(
            Point,
            'topic2',
            self.callback,
            10  # QoS profile
        )
        self.subscription  # Prevent unused variable warning

        # Subscribe to topic3 (std_msgs/String) for mission status
        self.subscription = self.create_subscription(
            String,
            'topic3',
            self.callback,
            10  # QoS profile
        )
        self.subscription  # Prevent unused variable warning

    def callback(self, msg):
        self.get_logger().info(f"Received :" +str(msg))

    #def callback(self, msg):
      #  self.get_logger().info(f"Received Location: x={msg.x}, y={msg.y}, z={msg.z}")

    #def callback(self, msg):
       # self.get_logger().info(f"Mission Status: {msg.data}")

def main(args=None):
    rclpy.init(args=args)
    node = BaseStationSubscriber()
    rclpy.spin(node)
    #node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

