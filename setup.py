from setuptools import setup, find_packages

from assis.utils import project_root

try:
    with open(f"{project_root}/readme.md", "r") as fh:
        long_description = fh.read()
except FileNotFoundError:
    long_description = "A doc generator for data engineering projects."

setup(
    name='assis',
    version='0.3.2',
    packages=find_packages(),
    description="A doc generator for data engineering projects.",
    long_description=long_description,
    include_package_data=True,
    author="Pedro H. Gonçalves",
    author_email="pedro_gonsalves@hotmail.com",
    url="https://github.com/pedrohgoncalvess/assis",
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'assis = assis.main:main',
        ],
    },
    install_requires=[
        "openai",
        "python-dotenv",
        "pyyaml"
    ],
)
