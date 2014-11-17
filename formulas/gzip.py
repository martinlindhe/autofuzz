# STATUS xxxx

class gzip:
    name = __name__
    home = "http://www.gzip.org/"

    scmOrigin = "git clone http://git.savannah.gnu.org/r/gzip.git"
    dataTypes = [
        "gz"
    ]

    target = "xxxx"
    targetParam = ""
    aflFuzzParam = ""

    clean = [
        "make distclean"
    ]

    build = [
        "./bootstrap",
        "CC=afl-gcc ./configure --disable-shared",
        "make"
    ]
