# STATUS works, but is very slow (7/sec)

# Nov 2014 - no problems found:
#         run time : 8 days, 3 hrs, 55 min, 58 sec        cycles done : 0
#    last new path : 0 days, 6 hrs, 36 min, 25 sec        total paths : 6382
#  last uniq crash : none seen yet                       uniq crashes : 0
#   last uniq hang : 1 days, 6 hrs, 5 min, 50 sec          uniq hangs : 6

class cppcheck:
    name = __name__
    home = "http://cppcheck.sourceforge.net/"
    scmOrigin = "git clone https://github.com/danmar/cppcheck.git {destination}"
    dataTypes = [
        "c"    # XXX also use cpp input sample
    ]

    target = "cppcheck"
    targetParam = "test.c"
    aflFuzzParam = "-f test.c"

    clean = [
        "make clean"
    ]

    build = [
        "CXX=afl-g++ make"
    ]
