#syntax=docker/dockerfile:1.4

# @see https://ros.org/reps/rep-0150.html
FROM ros:noetic-ros-core AS ros_base

RUN apt-get update && apt-get install -y \
    ros-noetic-foxglove-bridge \
    python3-pip && \
    rm -rf /var/lib/apt/lists/* && \
    pip3 install fire

#RUN wget -c https://raw.githubusercontent.com/qboticslabs/ros_install_noetic/master/ros_install_noetic.sh && chmod +x ./ros_install_noetic.sh && ./ros_install_noetic.sh

FROM ros_base AS ros_core

CMD [ "roscore" ]

FROM ros_base AS ros_command

# /opt/ros/noetic/setup.bash
RUN echo "\nsource "/opt/ros/$ROS_DISTRO/setup.bash"" | sudo tee -a /root/.bashrc >/dev/null

COPY --link docker/commander/publish-test.sh /usr/local/bin/publish-test
COPY --link docker/commander/robot.py /usr/local/bin/robot

RUN chmod -R +x /usr/local/bin/publish-test /usr/local/bin/robot

WORKDIR /root

FROM ros_base AS ros_node

COPY --link docker/subscriber/listener.py /usr/local/bin/ros-listener.py
