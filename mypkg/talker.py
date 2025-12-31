import rclpy
from rclpy.node import Node
from person_msgs.srv import Query


def cb(request, response):
    if request.name == "名前":
        response.age = 19
    else:
        response.age = 200

    return response


def main():
    rclpy.init()
    node = Node("talker")

    node.create_service(Query, "query", cb)
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
