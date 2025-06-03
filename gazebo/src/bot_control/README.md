# bot_control

**bot_control** is a package to get the readings from LiDAR scan, and filter and view them.

## Getting Started

### Prerequisites
- bot_description
- bot_world

### Installation

Build the package using colcon build from the project directory:
   ```bash
   colcon build --packages-select bot_control
   ```

### Usage

1. Source the project directory:
   ```bash
   source install/setup.bash
   ```

2. Run the 'laser' launch file:
   ```bash
   ros2 launch bot_control laser.launch.py
   ```