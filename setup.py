#coding:utf8
from setuptools import setup
setup(
    name="DGLabMouseListener2",
    version=2.0,
    author="N/A",
    license="Apache",
    packages=["DGLabMouseListener2"],
    install_requires=[
        "requests",
        "websockets",
        "loguru"
        "pynput"
    ]
    )