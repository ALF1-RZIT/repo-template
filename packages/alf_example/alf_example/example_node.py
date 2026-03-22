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

"""
Przykładowy węzeł ROS2 dla projektu ALF (Unitree G1 EDU).

Plik ten stanowi punkt startowy dla nowej funkcjonalności.
Skopiuj ten pakiet, zmień nazwy i zacznij implementację od tego szablonu.

Jak działa ten węzeł?
---------------------
1. Inicjalizacja: węzeł rejestruje się w systemie ROS2 pod
   nazwą 'alf_example_node'.
2. Publisher: co sekundę publikuje wiadomość tekstową (std_msgs/String)
   na topicu '/alf/status'.
3. Timer: wywołuje timer_callback() z częstotliwością 1 Hz (raz na sekundę).

Jak uruchomić (po zbudowaniu pakietu):
---------------------------------------
    ros2 run alf_example example_node

Jak obserwować publikowane wiadomości:
---------------------------------------
    ros2 topic echo /alf/status

Jak sprawdzić informacje o węźle:
----------------------------------
    ros2 node info /alf_example_node
"""

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class ExampleNode(Node):
    """
    Przykładowy węzeł ROS2 — punkt startowy dla nowej funkcjonalności.

    Ten węzeł pokazuje minimalną strukturę pakietu ROS2 w Pythonie:
    - tworzenie publishera (nadawcy wiadomości),
    - tworzenie timera (cykliczne wywoływanie funkcji),
    - logowanie komunikatów (info / debug).

    Aby dostosować do swojej funkcjonalności:
    - zmień nazwę klasy i węzła (super().__init__('...'))
    - zmień temat (topic) i typ wiadomości w create_publisher(...)
    - zaimplementuj logikę w timer_callback() lub dodaj subscriber/serwis
    """

    def __init__(self):
        # Wywołanie konstruktora klasy bazowej Node z nazwą węzła.
        # Nazwa węzła musi być unikalna w obrębie systemu ROS2.
        super().__init__('alf_example_node')

        # Tworzenie publishera:
        #   - typ wiadomości: std_msgs/String
        #   - temat (topic): '/alf/status'
        #   - rozmiar kolejki (QoS depth): 10
        self.publisher_ = self.create_publisher(String, 'alf/status', 10)

        # Tworzenie timera — wywołuje timer_callback co 1 sekundę (1 Hz).
        timer_period = 1.0  # sekundy
        self.timer = self.create_timer(timer_period, self.timer_callback)

        self.get_logger().info('ALF Example Node uruchomiony.')

    def timer_callback(self):
        """Callback timera — wywoływany cyklicznie (co 1 sekundę)."""
        # Tworzenie wiadomości i ustawienie jej zawartości.
        msg = String()
        msg.data = 'ALF Example Node działa.'

        # Publikowanie wiadomości na topicu '/alf/status'.
        self.publisher_.publish(msg)

        # Logowanie na poziomie DEBUG (widoczne przy --log-level DEBUG).
        self.get_logger().debug(f'Opublikowano: "{msg.data}"')


def main(args=None):
    """Punkt wejścia programu — wymagany przez entry_points w setup.py."""
    # Inicjalizacja biblioteki rclpy (musi być wywołana przed użyciem ROS2).
    rclpy.init(args=args)

    node = ExampleNode()
    try:
        # Uruchomienie pętli zdarzeń — węzeł działa do momentu przerwania.
        rclpy.spin(node)
    except KeyboardInterrupt:
        # Ctrl+C — graceful shutdown.
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
