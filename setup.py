import setuptools
import os.path

import sm

_APP_PATH = os.path.dirname(sm.__file__)

with open(os.path.join(_APP_PATH, 'resources', 'README.rst')) as f:
      long_description = f.read()

with open(os.path.join(_APP_PATH, 'resources', 'requirements.txt')) as f:
      install_requires = [s.strip() for s in f.readlines()]

setuptools.setup(
    name='splitmedia',
    version=sm.__version__,
    description="Split one media file into many based on a list of offsets",
    long_description=long_description,
    classifiers=[],
    keywords='split audio video',
    author='Dustin Oprea',
    author_email='myselfasunder@gmail.com',
    url='https://github.com/dsoprea/splitmedia',
    license='GPL 2',
    packages=setuptools.find_packages(exclude=['dev']),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    package_data={
        'sm': [
            'resources/README.rst',
            'resources/requirements.txt',
        ],
    },
    scripts=[
        'sm/resources/scripts/splitmedia',
    ],
)