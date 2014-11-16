
class giflib:
    name = __name__
    home = "http://giflib.sourceforge.net/"
    scmOrigin = "git clone git://git.code.sf.net/p/giflib/code"
    dataTypes = [
        "gif"
    ]

    target = "util/giftext"
    targetParam = ""

    clean = [
        "make distclean"
    ]

    build = [
        "CC=afl-gcc ./autogen.sh --disable-shared",
        "make"
    ]
