# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os


version = '0.1-dev'

here = os.path.abspath(os.path.dirname(__file__))

def read_file(*pathes):
    path = os.path.join(here, *pathes)
    if os.path.isfile(path):
        with open(path, 'r') as desc_file:
            return desc_file.read()
    else:
        return ''

desc_files = (('README.rst',), ('docs', 'CHANGES.rst'),
                ('docs', 'CONTRIBUTORS.rst'))

long_description = '\n\n'.join([read_file(*pathes) for pathes in desc_files])

install_requires=['setuptools', 'zc.buildout>=2.12.0']

entry_point = 'mr.nitpicker:install'
entry_points = {"zc.buildout.extension": ["default = %s" % entry_point]}

setup(name='mr.nitpicker',
      version=version,
      description="Buildout extension that builds versions section from requirements.txt",
      long_description=long_description,
      platforms = ["any"],
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        ],
      keywords="buildout",
      author="Godefroid Chapelle",
      author_email="gotcha@bubblenet.be",
      url="",
      license="ZPL",
      packages=find_packages("src"),
      package_dir = {"": "src"},
      namespace_packages=["mr"],
      include_package_data=True,
      zip_safe=True,
      install_requires=install_requires,
      entry_points=entry_points,
      )

# vim:set et sts=4 ts=4 tw=80:
