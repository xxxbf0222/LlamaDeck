from setuptools import setup, find_packages

setup(
    name='llama-gym',
    version='1.0.0',
    author="bufan0222",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'llama-gym = llamashepherd.main:main',
        ],
    },
)

