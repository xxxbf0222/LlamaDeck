from setuptools import setup, find_packages

VERSION = "1.0.0"
DESCRIPTION = "llama-deck is a command-line tool for quickly managing and experimenting with multiple versions of llama inference implementations. It can help you quickly filter and download different llama implementations) and llama2-like transformer-based LLM models. We also provide some images based on some implementations, which can be easily deploy and run through our tool. Inspired by llama2.c project."


setup(
    name='llama-deck',
    version=VERSION,
    description=DESCRIPTION,
    author="bufan0222",
    long_description_content_type="text/markdown",
    long_description=open("README.md",encoding="UTF8").read(),
    url="https://github.com/xxxbf0222/LlamaDeck",
    keywords=["python","llama","llama2","LLM","llama2.c","llama2.java","docker","llama-deck"],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'llama-deck = llamadeck.main:main',
        ],
    },
)

