# STATUS runs

# Nov 2014 - no problems found:
#        run time : 9 days, 6 hrs, 54 min, 57 sec        cycles done : 2352
#   last new path : 8 days, 22 hrs, 51 min, 38 sec       total paths : 37
# last uniq crash : none seen yet                       uniq crashes : 0
#  last uniq hang : 3 days, 15 hrs, 30 min, 54 sec        uniq hangs : 2


class xz:
    name = __name__
    home = "http://tukaani.org/xz/"
    scmOrigin = "git clone http://git.tukaani.org/xz.git {destination}"
    dataTypes = [
        "xz"
    ]

    target = "src/xzdec/xzdec"    # TODO theres also lzmadec
    targetParam = ""
    aflFuzzParam = ""

    clean = [
        "make distclean"
    ]

    build = [
        "./autogen.sh",
        "CC=afl-gcc ./configure --disable-shared",
        "make"
    ]
