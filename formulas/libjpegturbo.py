# STATUS runs

# Nov 2014:
#        run time : 9 days, 11 hrs, 18 min, 34 sec       cycles done : 0
#   last new path : 0 days, 6 hrs, 31 min, 29 sec        total paths : 2776
# last uniq crash : none seen yet                       uniq crashes : 0
#  last uniq hang : 9 days, 3 hrs, 44 min, 38 sec         uniq hangs : 500+

class libjpegturbo:
    name = "libjpeg-turbo"
    home = "http://libjpeg-turbo.virtualgl.org/"
    scmOrigin = "svn checkout svn://svn.code.sf.net/p/libjpeg-turbo/code/trunk {destination}"
    dataTypes = [
        "jpeg"
    ]

    target = "djpeg"
    targetParam = ""
    aflFuzzParam = ""

    clean = [
        "make distclean"
    ]

    build = [
        "autoreconf -fiv",
        "CC={AFL_CC} ./configure --disable-shared",
        "make"
    ]
