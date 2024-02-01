#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pythonProject 
@File    ：setup.py
@IDE     ：PyCharm 
@Author  ：XX
@Date    ：2024/2/1 10:19 
'''
from setuptools import setup, find_packages

setup(
    name='ckpe',
    version='0.1.0',
    description='python toolkit',
    url='https://github.com/jesuswa/ckpe.git',
    author='wh-ckpe01',
    author_email='13673146262@163.com',
    license='MIT',
    keywords='python toolkit utils',
    packages=find_packages(),  # 这会自动找到所有子包
    package_data={
        # 如果你有在任何包下的文件夹中的文件需要包含进来，可以这样指定
        '': ['*.txt', '*.json'],  # 包括所有目录下的.txt和.json文件
    },
    include_package_data=True,  # 这告诉setuptools包含那些在MANIFEST.in中指定的文件
    install_requires=[
        'pkuseg',  # 确保这是你项目需要的依赖包
    ],
    python_requires='>=3',
)