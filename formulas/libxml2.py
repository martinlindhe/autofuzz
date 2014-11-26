# STATUS runs

# Nov 2014:
#        run time : 8 days, 0 hrs, 6 min, 28 sec         cycles done : 0
#   last new path : 0 days, 3 hrs, 28 min, 41 sec        total paths : 3426
# last uniq crash : none seen yet                       uniq crashes : 0
#  last uniq hang : 0 days, 23 hrs, 15 min, 58 sec        uniq hangs : 3

class libxml2:
    name = __name__
    home = "http://xmlsoft.org/"
    scmOrigin = "git clone git://git.gnome.org/libxml2"
    dataTypes = [
        "xml"
    ]

    target = "testReader"
    targetParam = "test.xml"
    aflFuzzParam = "-f test.xml"

    clean = [
        "make distclean"
    ]

    build = [
        "CC=afl-gcc ./autogen.sh --disable-shared",
        "make"
    ]
