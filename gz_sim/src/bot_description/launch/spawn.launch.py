#   Shubh Khandelwal

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
import os

def generate_launch_description():

    bot_description = get_package_share_directory("bot_description")
    ros_gz_sim = get_package_share_directory("ros_gz_sim")

    world = LaunchConfiguration("world")
    x_pose = LaunchConfiguration("x_pose", default = "0.0")
    y_pose = LaunchConfiguration("y_pose", default = "0.0")

    sdf_path = os.path.join(bot_description, "models", "bot.sdf")

    gz_server_node = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(ros_gz_sim, "launch", "gz_sim.launch.py")
        ),
        launch_arguments = {
            "gz_args": ["-r -s -v2 ", world],
            "on_exit_shutdown": "true"
        }.items()
    )

    gz_client_node = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(ros_gz_sim, "launch", "gz_sim.launch.py")
        ),
        launch_arguments = {
            "gz_args": "-g -v2 "
        }.items()
    )

    spawner_node = Node(
        package = "ros_gz_sim",
        executable = "create",
        arguments = [
            "-name", "bot",
            "-file", sdf_path,
            "-x", x_pose,
            "-y", y_pose,
            "-z", "0.1"
        ],
        output = "screen"
    )

    bridge_parameters = os.path.join(
        bot_description,
        "config",
        "ros_gz_bridge.yaml"
    )

    ros_gz_bridge_node = Node(
        package = "ros_gz_bridge",
        executable = "parameter_bridge",
        arguments = [
            "--ros-args",
            "-p",
            f"config_file:={bridge_parameters}"
        ],
        output = "screen"
    )

    ros_gz_image_bridge_node = Node(
        package = "ros_gz_image",
        executable = "image_bridge",
        arguments = ["/camera/image_raw"],
        output = "screen",
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            "world",
            default_value = "empty.sdf",
            description = "Specify world for Gazebo simulation"
        ),
        DeclareLaunchArgument(
            "x_pose",
            default_value = "0.0",
            description = "Specify namespace of the robot"
        ),
        DeclareLaunchArgument(
            "y_pose",
            default_value = "0.0",
            description = "Specify namespace of the robot"
        ),
        gz_server_node,
        gz_client_node,
        spawner_node,
        ros_gz_bridge_node,
        ros_gz_image_bridge_node
    ])