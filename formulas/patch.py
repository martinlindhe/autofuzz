# STATUS runs


# Dec 2014
#        run time : 11 days, 21 hrs, 1 min, 56 sec       cycles done : 0
#   last new path : 0 days, 6 hrs, 55 min, 29 sec        total paths : 1957
# last uniq crash : 4 days, 12 hrs, 4 min, 23 sec       uniq crashes : 36
#  last uniq hang : 0 days, 16 hrs, 27 min, 48 sec        uniq hangs : 110


class patch:
    name = __name__
    home = "https://savannah.gnu.org/projects/patch/"
    scmOrigin = "git clone git://git.savannah.gnu.org/patch.git {destination}"
    dataTypes = [
        "txt"
    ]

    target = "src/patch"
    targetParam = ""
    aflFuzzParam = ""

    clean = [
        "make distclean"
    ]

    build = [
        "./bootstrap",
        "CC=afl-gcc ./configure",
        "make"
    ]
