#!/usr/bin/env python3

import fire
import rospy
from std_msgs.msg import String

class Robot(object):
    """Subset of commands for the robot.

    Commands:
        - move
    """

    def move(self, dir: str, paces: int):
        """Move the robot.

        Example:
            robot move forward 10

        :param dir: The direction to move - forward, backward, left, right
        :param paces: The number of paces to move. Must be positive.
        """

        dirs = ['forward', 'backward', 'left', 'right']

        if not dir in dirs:
            print("Invalid direction. Valid directions are: forward, backward, left, right")
            return

        if paces < 0:
            print("Invalid number of paces. Paces must be positive.")
            return

        command = str('Move {dir} {paces}').format(
            dir=dir,
            paces=paces
        )

        pub = rospy.Publisher('move', String, queue_size=10)
        rospy.init_node('talker', anonymous=True)
        pub.publish(command)

        print("Movement request sent: {command}".format(command=command))

if __name__ == '__main__':
    fire.Fire(Robot)