#!/bin/bash

rostopic pub /move std_msgs/String 'data: hello' -r 1
