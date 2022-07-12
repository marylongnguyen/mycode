#!/usr/bin/env python3

import shutil
import os

os.chdir('/home/student/mycode/')
shutil.move('raynor.obj', 'ceph_storage/')

#Prompt the user for a new name for the kerrigan.obj file
xname = input('What is the new name for kerrigan.obj? ')

#Rename the current kerrigan.obj file with user's new name 
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

