from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """Return list of requirements from requirements.txt"""
    with open(file_path) as f:
        return [line.strip() for line in f if line.strip() and line.strip() != "-e ."]

setup(
    name="mlproject",
    author="Krish",
    author_email="meghana.vbm@gmail.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=get_requirements("requirements.txt"),
)
