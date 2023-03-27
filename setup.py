# -*- coding: utf-8 -*-

from setuptools import setup

# def readme():
#     with open("README.md") as f:
#         return f.read()

setup(name="drawBotEasing",
      version="0.1",
      description="A small library of easing methods and animations helpers for DrawBot (or more)…",
      long_description="TBD",
      classifiers=[
        "Development Status :: 4 - Beta",
        "License :: Other/Proprietary License",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Build Tools",
      ],
      author="Mathieu Reguer",
      author_email="mathieu.reguer@gmail.com",
      license="All rights reserved",
      packages=[
        "drawBotEasing",
        ],
      install_requires=[
        #"drawBot",
      ],
      include_package_data=True,
      zip_safe=False)
