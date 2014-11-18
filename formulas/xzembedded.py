# STATUS works

# status when 1st run was stopped:
#         run time : 1 days, 2 hrs, 17 min, 57 sec        cycles done : 778
#    last new path : 1 days, 1 hrs, 25 min, 32 sec        total paths : 32
#  last uniq crash : none seen yet                       uniq crashes : 0
#   last uniq hang : none seen yet                         uniq hangs : 0


class xzembedded:
    name = __name__
    home = "http://tukaani.org/xz/"
    scmOrigin = "git clone http://git.tukaani.org/xz-embedded.git"
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
