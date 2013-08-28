#! /usr/bin/env python

import commands
import os
import sys
import subprocess

print 'Hello world'
cwd = '/home/git_scripts/' + sys.argv[1]
print cwd
lastChangeDate = subprocess.Popen("/usr/bin/git log --pretty=format:\"%ad\" ~/get_scripts/test.c", shell=True)
print lastChangeDate
