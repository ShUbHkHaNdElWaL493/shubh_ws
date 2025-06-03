#   Shubh Khandelwal

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, ExecuteProcess, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
import xacro
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node

def generate_launch_description():

    use_sim_time = LaunchConfiguration('use_sim_time')

    pkg_path = os.path.join(get_package_share_directory('bot_world'))
    urdf_xacro = os.path.join(pkg_path,'description','bot_structure.urdf.xacro')
    robot_description_config = xacro.process_file(urdf_xacro)
    
    params = {'robot_description': robot_description_config.toxml(), 'use_sim_time': use_sim_time}

    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[params]
    )

    world_path = "/home/ayush/Documents/ayush_ws/src/bot_world/worlds/world1.world"
    gazebo_node = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')]),
        launch_arguments={'world': world_path}.items()
    )

    spawner_node = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-topic', 'robot_description', '-entity', 'o'],
        output='screen'
    )
    

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='true',
            description='Use sim time if true'),

            robot_state_publisher_node,
            gazebo_node,
            spawner_node,
        ])