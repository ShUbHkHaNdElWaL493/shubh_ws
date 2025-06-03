#   Shubh Khandelwal

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():

    use_sim_time = LaunchConfiguration("use_sim_time")
    
    teleop_node = Node(
        package = "teleop_twist_keyboard",
        executable = "teleop_twist_keyboard",
        name = "teleop_twist_keyboard",
        prefix = "xterm -e",
        output = "screen",
        parameters = [{
            "use_sim_time" : use_sim_time
        }],
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            "use_sim_time",
            default_value = "true",
            description = "Use simulation (Gazebo) clock if true"
        ),
        teleop_node
    ])