# Copyright (c) 2024, APT Group, Department of Computer Science,
# The University of Manchester.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

# http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup, find_packages

VERSION = "1.0.0.post1"
DESCRIPTION = "Llama-Deck is a command-line tool for quickly managing and experimenting with multiple versions of llama inference implementations. It can help you quickly filter and download different llama implementations) and llama2-like transformer-based LLM models. We also provide some images based on some implementations, which can be easily deploy and run through our tool. Inspired by llama2.c project."


setup(
    name='llama-deck',
    version=VERSION,
    description=DESCRIPTION,
    author="bufan0222",
    long_description_content_type="text/markdown",
    long_description=open("PYPI_DESCRIPTION.md",encoding="UTF8").read(),
    url="https://github.com/xxxbf0222/LlamaDeck",
    keywords=["python","llama","llama2","LLM","llama2.c","llama2.java","docker","llama-deck"],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'llama-deck = llamadeck.main:main',
        ],
    },
)

