from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    pkg = 'simple_car_description'
    urdf_file = 'simple_car.urdf'
    urdf_path = os.path.join(
        get_package_share_directory(pkg), 'urdf', urdf_file)

    with open(urdf_path, 'r') as infp:
        robot_desc = infp.read()

    return LaunchDescription([
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui'
        ),
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            output='both',
            parameters=[{
                'robot_description': robot_desc
            }]
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            output='screen',
            arguments=['-d', os.path.join(
                get_package_share_directory(pkg),
                'rviz',
                'car_view.rviz'  # we will optionally create this
            )]
        ),
    ])

