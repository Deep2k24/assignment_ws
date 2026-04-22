import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # Use the absolute path to the source directory as recommended in the FAQ
    map_yaml_file = '/home/deep/assignment_ws/src/ros_nav2_assignment/testbed_bringup/maps/testbed_world.yaml'

    return LaunchDescription([
        # 1. Map Server Node
        Node(
            package='nav2_map_server',
            executable='map_server',
            name='map_server',
            output='screen',
            parameters=[{'yaml_filename': map_yaml_file},
                        {'use_sim_time': True}]
        ),
        
        # 2. Lifecycle Manager Node
        Node(
            package='nav2_lifecycle_manager',
            executable='lifecycle_manager',
            name='lifecycle_manager_map',
            output='screen',
            parameters=[{'use_sim_time': True},
                        {'autostart': True},
                        {'node_names': ['map_server']}]
        )
    ])