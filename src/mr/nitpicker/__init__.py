# -*- coding: utf-8 -*-

import zc.buildout.easy_install
import os.path

"""
nitpicker
------------------------------
Buildout extension that builds versions section from requirements.txt

"""

def read_from_requirements(buildout):
    filename = os.path.join(buildout['buildout']['directory'],
        'requirements.txt')
    versions = dict()
    with open(filename) as req:
        for line in req:
            name, version = line[:-1].split('==')
            versions[name]=version
    return versions

def enable(old_setup_directories):
    def setup_directories(self):
        versions = read_from_requirements(self)
        zc.buildout.easy_install.default_versions(versions)
        old_setup_directories(self)
    return setup_directories


def install(buildout):

    zc.buildout.buildout.Buildout._setup_directories = enable(
        zc.buildout.buildout.Buildout._setup_directories)


  

# vim:set et sts=4 ts=4 tw=80:
