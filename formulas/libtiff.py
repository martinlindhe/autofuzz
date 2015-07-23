# STATUS runs


# Dec 2014
#        run time : 24 days, 21 hrs, 33 min, 17 sec      cycles done : 86
#   last new path : 0 days, 5 hrs, 59 min, 32 sec        total paths : 1250
# last uniq crash : 1 days, 12 hrs, 43 min, 12 sec      uniq crashes : 12
#  last uniq hang : 13 days, 17 hrs, 59 min, 48 sec       uniq hangs : 4

class libtiff:
    name = __name__
    home = "http://www.remotesensing.org/libtiff/"
    scmOrigin = "cvs -d :pserver:cvsanon:@cvs.maptools.org:/cvs/maptools/cvsroot login && cvs -z3 -d :pserver:cvsanon:@cvs.maptools.org:/cvs/maptools/cvsroot co -d {destination} -P libtiff"
    dataTypes = [
        "tiff"
    ]

    target = "tools/tiffdump"
    targetParam = "test.tif"
    aflFuzzParam = "-f test.tif"

    clean = [
        "make distclean"
    ]

    build = [
        "./autogen.sh",
        "./configure CC={AFL_CC} CXX={AFL_CXX} --disable-shared",
        "make"
    ]
