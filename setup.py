"""setup file"""
from setuptools import setup

setup(
    name="flask-react-boilerplate",
    packages=["boilerplate"],
    include_package_data=True, #seems necessary
    install_requires=[
        "flask"
    ]
)
