#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import print_function

import os

def is_in_profile(file, content):
    reader = open(file)

    line = reader.readline()

    while line != '' and line != None:
        if -1 != line.find(content):
            print(line)
            reader.close()
            return True
        line = reader.readline()
    reader.close()
    return False

def set_to_profile(cmd):
    path = os.path.expanduser('~')
    profile = path + '/' + '.profile'

    is_existed = is_in_profile(profile, cmd)
    if False == is_existed:
        os.system("echo '' >> ~/.profile")
        profile_cmd = "echo '%s' >> ~/.profile" % cmd
        os.system(profile_cmd)