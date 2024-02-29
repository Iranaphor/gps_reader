from setuptools import setup
from glob import glob
import os

package_name = 'gps_reader'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', [f'resource/{package_name}']),
        (f'share/{package_name}', ['package.xml'])
    ],
    zip_safe=True,
    maintainer='james',
    maintainer_email='primordia@live.com',
    description='Package for reading gps data',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'vfan.py = gps_reader.vfan:main'
        ],
    },
)
