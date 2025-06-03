#   Shubh Khandelwal

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
import xacro

def generate_launch_description():

    use_sim_time = LaunchConfiguration('use_sim_time')

    pkg_path = os.path.join(get_package_share_directory('bot_control'))
    urdf_xacro = os.path.join(pkg_path,'description','bot_structure.urdf.xacro')
    robot_description_config = xacro.process_file(urdf_xacro)
    
    params = {'robot_description': robot_description_config.toxml(), 'use_sim_time': use_sim_time}
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[params]
    )

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', os.path.join(pkg_path, 'config', 'config.rviz')]
    )

    laser_node = Node(
            package='bot_control',
            executable='reading_laser',
            name='reading_laser_node',
            output='screen'
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use sim time if true'
        ),
        robot_state_publisher_node,
        rviz_node,
        laser_node
    ])