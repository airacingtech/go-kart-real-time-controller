# Copyright 2022 Triton AI

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    gkc_config = os.path.join(
        get_package_share_directory('tai_gokart_controller'),
        'param',
        'tai_gokart_controller_param.yaml'
    )
    return LaunchDescription([
        Node(
            package='tai_gokart_controller',
            executable='tai_gokart_controller_node',
            name='tai_gokart_controller_node',
            parameters=[gkc_config],
            remappings=[
                ('steering_report', '/vehicle/steering_report'),
                ('vehicle_cmd', '/auto/raw_command'),
            ],
            emulate_tty=True,
            output='screen'
        ),
    ])
