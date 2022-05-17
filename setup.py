"""This file and its contents are licensed under the Apache License 2.0. Please see the included NOTICE for copyright information and LICENSE for a copy of the license.
"""
import setuptools
import singularity_loop
import sys

print(singularity_loop.package_name, singularity_loop.__version__)

# Readme
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

# Module dependencies
requirements, dependency_links = [], []
with open('requirements.txt') as f:
    for line in f.read().splitlines():
        if line.startswith('-e git+'):
            dependency_links.append(line.replace('-e ', ''))
        else:
            requirements.append(line)

setuptools.setup(
    name=singularity_loop.package_name,
    version=singularity_loop.__version__,
    author='RBG.AI',
    author_email="hello@rbg.ai",
    description='Singularity Loop',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='www.rbg.ai',
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    install_requires=requirements,
    dependency_links=dependency_links,
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'singularity-loop=singularity_loop.server:main',
        ],
    },
    extras_require={
        'mysql': ['mysqlclient']
    }
)
