"""
Install module "sanitize".
"""
from setuptools import setup, find_packages


setup(
    name="sanitize",
    version="0.1.0",
    packages=find_packages(
        where="sanitize",
    ),
    install_requires=[
        "click==8.1.3",
        "setuptools==67.2.0",
        "rich==13.3.1",
        "fastapi",
        "uvicorn[standard]",
    ],
)
