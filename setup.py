#!/usr/bin/env python
# -*- coding:utf-8 -*-

from setuptools import setup, find_packages
        
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# see https://packaging.python.org/tutorials/packaging-projects/
setup(
#     固定部分
    name="kdGUI",
    version="1.0.0",
    author="bkdwei",
    author_email="bkdwei@163.com",
    maintainer="韦坤东",
    maintainer_email="bkdwei@163.com",
    long_description=long_description,
#     long_description_content_type="text/markdown",
    url="https://github.com/bkdwei/kdGUI",
    license="GPLv3+",
    platforms=["any"],
    
#     需要安装的依赖
    install_requires=[],
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,

#     可变部分
    description="",
    keywords=("tkinter", "ui"),
#   see  https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: X11 Applications :: Qt",
        "Intended Audience :: End Users/Desktop",
        "Natural Language :: Chinese (Simplified)",
        "Topic :: Software Development :: Code Generators",
        "Programming Language :: Python :: 3",
        " License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
    ]
)
