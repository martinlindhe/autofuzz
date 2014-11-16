#!/usr/bin/env python3
#
# tool to find issues with current setup

# TODO rework to python2

# TODO afl only runs on linux
from lib.OsxProbe import *


probe = OsxProbe()

if not probe.IsSupported():
    sys.exit()

# TODO add a OsxExecutableProbe, that detects 32/64 bit binaries

# file /usr/bin/gcc
# /usr/bin/gcc: Mach-O 64-bit executable x86_64


# TODO make sure afl-gcc 0.45b or newer is installed (in path) and see if its 32 or 64bit build


# TODO make sure "git" command is available
