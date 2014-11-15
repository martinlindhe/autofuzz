#!/usr/bin/env python3

import sys


def get_class(kls):
    parts = kls.split('.')
    module = ".".join(parts[:-1])
    m = __import__(module)
    for comp in parts[1:]:
        m = getattr(m, comp)
    return m

# TODO take 1 parameter, formula name
formulaName = "giflib"

try:
    formula = get_class("formulas." + formulaName + "." + formulaName)
except ImportError:
    print("ERROR: No such formula " + formulaName)
    sys.exit()


print(formula)

if formula.scm != "git":
    print("ERROR: unsupported scm: " + formula.scm)
    sys.exit()

# XXX 1. initial git checkout to .cache/giflib
