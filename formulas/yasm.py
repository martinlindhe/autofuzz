# STATUS runs

# Dec 2014:
#        run time : 24 days, 21 hrs, 21 min, 40 sec      cycles done : 0
#   last new path : 0 days, 4 hrs, 25 min, 10 sec        total paths : 11.5k
# last uniq crash : 1 days, 12 hrs, 31 min, 44 sec      uniq crashes : 17
#  last uniq hang : 0 days, 11 hrs, 5 min, 20 sec         uniq hangs : 95

class yasm:
    name = __name__
    home = "http://yasm.tortall.net/"
    scmOrigin = "git clone https://github.com/yasm/yasm.git {destination}"
    dataTypes = [
        "txt"
    ]

    target = "yasm"
    targetParam = "test.asm"
    aflFuzzParam = "-f test.asm"

    clean = [
        "make distclean"
    ]

    build = [
        "CC=afl-gcc ./autogen.sh",
        "make"
    ]
