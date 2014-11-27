# STATUS runs

# Nov 2014 - no problems found:
#        run time : 8 days, 3 hrs, 52 min, 41 sec        cycles done : 3087
#   last new path : 5 days, 22 hrs, 29 min, 25 sec       total paths : 33
# last uniq crash : none seen yet                       uniq crashes : 0
#  last uniq hang : none seen yet                         uniq hangs : 0

class xzembedded:
    name = __name__
    home = "http://tukaani.org/xz/"
    scmOrigin = "git clone http://git.tukaani.org/xz-embedded.git {destination}"
    dataTypes = [
        "xz"
    ]

    target = "userspace/xzminidec"
    targetParam = ""
    aflFuzzParam = ""

    clean = [
        "cd userspace; make clean"
    ]

    build = [
        "cd userspace; make CC=afl-gcc"
    ]
