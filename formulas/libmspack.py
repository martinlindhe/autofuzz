# STATUS runs


# Dec 2014:
#        run time : 12 days, 21 hrs, 27 min, 17 sec      cycles done : 541
#   last new path : 9 days, 16 hrs, 56 min, 8 sec        total paths : 118
# last uniq crash : none seen yet                       uniq crashes : 0
#  last uniq hang : 10 days, 9 hrs, 37 min, 34 sec        uniq hangs : 10

class libmspack:
    name = __name__
    home = "http://www.cabextract.org.uk/libmspack/"
    scmOrigin = "svn checkout svn://svn.code.sf.net/p/libmspack/code/libmspack/trunk/ {destination}"

    dataTypes = [
        "cab"  # XXX also handles other formats
    ]

    target = "test/expand"
    targetParam = "test.cab test.out"
    aflFuzzParam = "-f test.cab"

    clean = [
        "make distclean"
    ]

    build = [
        "./configure --disable-shared CC={AFL_CC} CXX={AFL_CXX}",
        "make"
    ]
