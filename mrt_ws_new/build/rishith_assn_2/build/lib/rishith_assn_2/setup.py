import os
from golb import glob
from setuptools import find_packages, setup
from setuptools import setup

package_name = 'rishith_assn_2'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share',package_name,'launch'),(
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rishith',
    maintainer_email='rishithgupta01@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'd_rover1 = rishith_assn_2.d_rover1:main',
        'd_rover2 = rishith_assn_2.d_rover2:main',
        'd_rover3 = rishith_assn_2.d_rover3:main',
        'd_rover4 = rishith_assn_2.d_rover4:main'
        ],
    },
)
