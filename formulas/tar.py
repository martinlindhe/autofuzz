# STATUS runs

# NOTE: needs --disable-gcc-warnings to build with gcc 4.7.2/Debian

# Dec 2014:
#        run time : 24 days, 20 hrs, 20 min, 22 sec      cycles done : 225
#   last new path : 0 days, 1 hrs, 34 min, 55 sec        total paths : 1141
# last uniq crash : none seen yet                       uniq crashes : 0
#  last uniq hang : 13 days, 17 hrs, 50 min, 14 sec       uniq hangs : 4

class tar:
    name = __name__
    home = "https://www.gnu.org/software/tar/"
    scmOrigin = "git clone git://git.savannah.gnu.org/tar.git {destination}"
    dataTypes = [
        "tar"
    ]

    target = "src/tar"
    targetParam = "x"
    aflFuzzParam = ""

    clean = [
        "make distclean"
    ]

    build = [
        "./bootstrap",
        "./configure CC={AFL_CC} --disable-gcc-warnings",
        "make"
    ]
