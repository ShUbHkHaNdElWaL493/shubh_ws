#   Shubh Khandelwal

from ament_index_python import get_package_share_directory
from launch import LaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import IncludeLaunchDescription
from launch_ros.actions import Node
import os

def generate_launch_description():

    bot_control = get_package_share_directory("bot_control")
    bot_description = get_package_share_directory("bot_description")
    bot_world = get_package_share_directory("bot_world")

    rviz_config = os.path.join(bot_control, "config", "config.rviz")
    world = os.path.join(bot_world, "worlds", "custom_world.world")

    spawner_node = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(bot_description, "launch", "spawn.launch.py")),
        launch_arguments = {
            "world" : world
        }.items()
    )

    rviz_node = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(bot_description, "launch", "rviz.launch.py")),
        launch_arguments = {
            "rviz_config" : rviz_config
        }.items()
    )

    laser_node = Node(
        package = "bot_control",
        executable = "laser_node",
        name = "laser_node",
        output = "screen"
    )

    return LaunchDescription([
        spawner_node,
        rviz_node,
        laser_node
    ])