#!/usr/bin/env python

import os
import sys
import subprocess


def get_class(kls):
    parts = kls.split('.')
    module = ".".join(parts[:-1])
    m = __import__(module)
    for comp in parts[1:]:
        m = getattr(m, comp)
    return m


def run_command(command):
    try:
        res = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError as e:
        print("command returned error code " + str(e.returncode))
        print("    - output: " + e.output)
        res = e.output

    return res


# TODO take 1 parameter, formula name
formulaName = "giflib"

try:
    formula = get_class("formulas." + formulaName + "." + formulaName)
except ImportError:
    print("ERROR: No such formula " + formulaName)
    sys.exit()

if formula.scm != "git":
    print("ERROR: unsupported scm: " + formula.scm)
    sys.exit()

print("### " + formulaName)

formulaPath = ".cache/" + formulaName

gitPath = formulaPath + "/.git"
if os.path.isdir(gitPath):
    # TODO if dir exist, do a "git pull" ? also make sure it is pristine
    print("Checkout found at " + gitPath + ", TODO do update?")
else:
    print("Checking out " + formula.origin + " ...")

    cmd = "git clone " + formula.origin + " .cache/" + formulaName
    # print("Command: " + cmd)
    run_command(cmd)
    print("done")

# set current working dir to formulaPath
os.chdir(formulaPath)
print("XXX changed cwd to " + os.getcwd())

for cleanCmd in formula.clean:
    print("CLEAN # " + cleanCmd)
    run_command(cleanCmd)

# TODO  do the build steps
for buildCmd in formula.build:
    print("BUILD # " + buildCmd)
    run_command(buildCmd)
