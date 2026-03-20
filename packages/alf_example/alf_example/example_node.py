# Copyright 2026 ALF1-RZIT
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class ExampleNode(Node):
    """Przykładowy węzeł ROS2 — punkt startowy dla nowej funkcjonalności."""

    def __init__(self):
        super().__init__('alf_example_node')
        self.publisher_ = self.create_publisher(String, 'alf/status', 10)
        timer_period = 1.0  # sekundy
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.get_logger().info('ALF Example Node uruchomiony.')

    def timer_callback(self):
        msg = String()
        msg.data = 'ALF Example Node działa.'
        self.publisher_.publish(msg)
        self.get_logger().debug(f'Opublikowano: "{msg.data}"')


def main(args=None):
    rclpy.init(args=args)
    node = ExampleNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
