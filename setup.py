from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="CELEBRITY DETECTOR and QA SYSTEM",
    version="0.1",
    author="mahendra varma",
    packages=find_packages(),
    install_requires = requirements,
)