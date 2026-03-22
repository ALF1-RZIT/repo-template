from setuptools import find_packages, setup

package_name = 'alf_example'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ALF1-RZIT Maintainers',
    maintainer_email='maintainers@alf1-rzit.example',
    description='Przykładowy pakiet ROS2 (Python) dla Unitree G1 EDU.',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'example_node = alf_example.example_node:main',
        ],
    },
)
