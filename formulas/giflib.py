# STATUS runs

# Nov 2014:
#        run time : 12 days, 10 hrs, 9 min, 51 sec       cycles done : 641
#   last new path : 3 days, 17 hrs, 33 min, 40 sec       total paths : 220
# last uniq crash : 0 days, 0 hrs, 16 min, 13 sec       uniq crashes : 1431
#  last uniq hang : none seen yet                         uniq hangs : 0


class giflib:
    name = __name__
    home = "http://giflib.sourceforge.net/"
    scmOrigin = "git clone git://git.code.sf.net/p/giflib/code {destination}"
    dataTypes = [
        "gif"
    ]

    target = "util/giftext"
    targetParam = ""
    aflFuzzParam = ""

    clean = [
        "make distclean"
    ]

    build = [
        "CC=afl-gcc ./autogen.sh --disable-shared",
        "make"
    ]
