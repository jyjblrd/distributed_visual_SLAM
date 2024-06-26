from setuptools import find_packages, setup

package_name = 'motion_controller'
submodules = 'motion_controller/helpers'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name, submodules],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='joshuabird',
    maintainer_email='jyjbird@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'collision_avoidance = motion_controller.collision_avoidance:main',
            'follow_the_leader = motion_controller.follow_the_leader:main'
        ],
    },
)
