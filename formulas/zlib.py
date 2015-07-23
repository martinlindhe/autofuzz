# STATUS runs

# XXX unsure if its proper, only found 4 paths

# Nov 2014:
#        run time : 9 days, 9 hrs, 59 min, 30 sec        cycles done : 61.1k
#   last new path : 9 days, 9 hrs, 59 min, 29 sec        total paths : 4
# last uniq crash : none seen yet                       uniq crashes : 0
#  last uniq hang : 8 days, 3 hrs, 37 min, 13 sec         uniq hangs : 1

class zlib:
    name = __name__
    home = "http://www.zlib.net/"
    scmOrigin = "git clone https://github.com/madler/zlib {destination}"
    dataTypes = [
        "deflate"
    ]

    target = "examples/zpipe"
    targetParam = "-d"
    aflFuzzParam = ""

    clean = [
        "make distclean"
    ]

    build = [
        "CC={AFL_CC} ./configure",
        "make",
        "{AFL_CC} -L. libz.so examples/zpipe.c -o examples/zpipe"
    ]
