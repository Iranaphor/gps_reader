import rclpy
from rclpy.node import Node
from sensor_msgs.msg import NavSatFix
import serial
import pynmea2

class GPSNode(Node):
    def __init__(self, device):
        super().__init__('gps_node')
        self.publisher_ = self.create_publisher(NavSatFix, 'gps', 10)
        self.serial_port = serial.Serial(device, 9600, timeout=2)
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        line = self.serial_port.readline().decode('ascii', errors='replace')
        if line.startswith('$GNGGA') or line.startswith('$GPGGA'):
            try:
                msg = pynmea2.parse(line)
                gps_msg = NavSatFix()
                gps_msg.latitude = msg.latitude
                gps_msg.longitude = msg.longitude
                gps_msg.altitude = msg.altitude
                self.publisher_.publish(gps_msg)
                self.get_logger().info('Publishing GPS Data: Latitude: %f, Longitude: %f' % (msg.latitude, msg.longitude))
            except pynmea2.ParseError:
                self.get_logger().warn('Could not parse GPS data')

def main(args=None):
    rclpy.init(args=args)
    gps_node = GPSNode('/dev/ttyACM0')
    rclpy.spin(gps_node)
    gps_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
