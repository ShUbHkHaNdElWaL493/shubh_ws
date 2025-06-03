#   Shubh Khandelwal

from ament_index_python import get_package_share_directory
from launch import LaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import IncludeLaunchDescription
import os

def generate_launch_description():

    bot_description = get_package_share_directory("bot_description")
    bot_world = get_package_share_directory("bot_world")

    world = os.path.join(bot_world, "worlds", "custom_world.world")

    spawner_node = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(bot_description, "launch", "spawn.launch.py")),
        launch_arguments = {
            "world" : world
        }.items()
    )

    return LaunchDescription([
        spawner_node
    ])