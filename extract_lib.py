# This file extracts all required libs into lib folder
import os

req_list = open("requirements.txt")

for req in req_list:
    cmd = "pip install -t lib " + req
    print "Running " + cmd
    os.system(cmd)
