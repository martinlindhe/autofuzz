# STATUS runs


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
        "./configure CC=afl-gcc CXX=afl-g++ --disable-shared",
        "make"
    ]
