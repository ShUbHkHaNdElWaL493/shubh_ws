#   Shubh Khandelwal

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
import os

def generate_launch_description():

    bot_description = get_package_share_directory("bot_description")

    rviz_config = LaunchConfiguration("rviz_config")
    use_sim_time = LaunchConfiguration("use_sim_time")

    urdf_path = os.path.join(bot_description, "models", "bot.urdf")

    with open(urdf_path, 'r') as urdf_file:
        robot_description = urdf_file.read()
    
    robot_state_publisher_node = Node(
        package = "robot_state_publisher",
        executable = "robot_state_publisher",
        name = "robot_state_publisher",
        output = "screen",
        parameters = [{
            "use_sim_time" : use_sim_time,
            "robot_description" : robot_description,
            "frame_prefix" : "/"
        }],
    )

    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        arguments=["-d", rviz_config],
        output="screen"
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            "use_sim_time",
            default_value = "true",
            description = "Use simulation (Gazebo) clock if true"
        ),
        DeclareLaunchArgument(
            "rviz_config",
            default_value = os.path.join(bot_description, "config", "config.rviz"),
            description = "Use simulation (Gazebo) clock if true"
        ),
        robot_state_publisher_node,
        rviz_node
    ])