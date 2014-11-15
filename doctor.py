#!/usr/bin/env python3

# TODO add a OsxExecutableProbe, that detects 32/64 bit binaries


from lib.OsxProbe import *


probe = OsxProbe()

if not probe.IsSupported():
    sys.exit()
