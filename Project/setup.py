# Setup script for packaging
from setuptools import setup, find_packages

setup(
    name='{project_name}',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'scikit-learn',
        'matplotlib'
    ],
)