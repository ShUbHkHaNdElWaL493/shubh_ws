# bot_description

**bot_description** is a package that contains the description of the robot.

## Getting Started

### Installation

Build the package using colcon build from the project directory:
   ```bash
   colcon build --packages-select bot_description
   ```

### Usage

1. Run the 'spawn' launch file to spawn the robot in an empty world:
   ```bash
   source install/setup.bash
   ros2 launch bot_description spawn.launch.py
   ```

2. Run the 'rviz' launch file to visualize the robot in rviz2 in another terminal:
   ```bash
   source install/setup.bash
   ros2 launch bot_description rviz.launch.py
   ```

3. Run the 'control' launch file to control the robot in another terminal:
   ```bash
   source install/setup.bash
   ros2 launch bot_description control.launch.py
   ```