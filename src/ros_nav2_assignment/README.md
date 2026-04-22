# Testbed Navigation Package

**Developer:** Deep Sonawane  
**Project:** ERIC Robotics ROS2 Navigation Assignment (Level 1)

## Overview
This package provides a modular implementation of the Nav2 stack for the Testbed-T1.0.0 robot. Instead of using the monolithic `nav2_bringup`, this package manually launches and manages the Map Server, AMCL Localization, and the Navigation servers (Planner, Controller, Behaviors, and BT Navigator).

## Approach
The navigation workflow was built step-by-step to ensure modularity:
1. **Map Loading:** Implemented via `nav2_map_server` to load the provided `testbed_world.yaml`.
2. **Localization:** Configured using `nav2_amcl` with an automated initial pose to match the Gazebo spawn coordinates.
3. **Navigation:** Utilized the Global Planner (Grid) and Local Planner (DWB) through independent server nodes, orchestrated by a Lifecycle Manager.
4. **Visualization:** A custom RViz configuration was created to overlay the Global and Local costmaps with proper transparency and Z-layering.

## Challenges & Solutions
* **Map File Paths:** Initially encountered issues with relative paths. Solved by using `get_package_share_directory` to ensure the launch files could locate maps regardless of the execution directory.
* **QoS Mismatch:** The `/particle_cloud` was not visible in RViz due to a Reliability Policy mismatch (Best Effort vs. Reliable). This was resolved by setting the RViz display to `Best Effort`.

## How to Run
1. **Simulation:** `ros2 launch testbed_bringup testbed_full_bringup.launch.py`
2. **Map Loader:** `ros2 launch testbed_navigation map_loader.launch.py`
3. **Localization:** `ros2 launch testbed_navigation localization.launch.py`
4. **Navigation:** `ros2 launch testbed_navigation navigation.launch.py`

*(Note: The navigation launch file will automatically open RViz with the correct configuration.)*

## Contact Info 
 - Name: Deep Sonawane
 - Contact number: 8669189617
 - Email Address: deepsonawane.robotics@gmail.com