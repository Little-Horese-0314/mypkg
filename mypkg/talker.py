#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from person_msgs.srv import Query


class PositionServer(Node):
    def __init__(self):
        super().__init__('position_server')

        self.x = 0
        self.y = 0

        self.create_service(Query, 'move', self.callback)
        self.get_logger().info('Position server started.')

    def callback(self, request, response):
        cmd = request.command.lower()

        if cmd == 'up':
            self.y += 1
        elif cmd == 'down':
            self.y -= 1
        elif cmd == 'right':
            self.x += 1
        elif cmd == 'left':
            self.x -= 1
        elif cmd == 'reset':
            self.x = 0
            self.y = 0

        response.x = self.x
        response.y = self.y

        self.get_logger().info(f'x={self.x}, y={self.y}')
        return response


def main():
    rclpy.init()
    node = PositionServer()
    rclpy.spin(node)
    rclpy.shutdown()
