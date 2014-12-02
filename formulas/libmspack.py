# STATUS builds, need .cab sample


class libmspack:
    name = __name__
    home = "http://www.cabextract.org.uk/libmspack/"
    scmOrigin = "svn checkout svn://svn.code.sf.net/p/libmspack/code/libmspack/trunk/ {destination}"

    dataTypes = [
        "cab"  # XXX also handles other formats
    ]

    target = "test/expand"  ## XXX is a wrapper shell script
    targetParam = ""
    aflFuzzParam = ""

    clean = [
        "make distclean"
    ]

    build = [
        "./configure --disable-shared CC=afl-gcc CXX=afl-g++",
        "make"
    ]
