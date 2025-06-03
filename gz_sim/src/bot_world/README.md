# bot_world

**bot_world** is a package that contains custom Gazebo worlds.

## Getting Started

### Prerequisites
- bot_description

### Installation

Build the package using colcon build from the project directory:
   ```bash
   colcon build --packages-select bot_world
   ```

### Usage

1. Source the project directory:
   ```bash
   source install/setup.bash
   ```

2. Run the 'spawn' launch file:
   ```bash
   ros2 launch bot_world spawn.launch.py
   ```