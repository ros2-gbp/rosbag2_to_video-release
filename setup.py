from setuptools import setup

package_name = 'rosbag2_to_video'

setup(
    name=package_name,
    version='1.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Ivan Santiago Paunovic',
    author_email='ivanpauno@ekumenlabs.com',
    maintainer='Błażej Sowa',
    maintainer_email='blazej@ficionlab.pl',
    description='Command line tool to create a video from a rosbag recording',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'rosbag2_to_video = rosbag2_to_video:main',
        ],
        'ros2bag.verb': [
            'to_video = rosbag2_to_video.ros2bag_verb:ToVideo',
        ],
    },
)
