from setuptools import find_packages, setup

package_name = 'rishith_assn_2'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
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
        'd_rover4 = rishith_assn_2.d_rover4:main',
        'basestation  = rishith_assn_2.basestation:main'
        ],
    },
)
