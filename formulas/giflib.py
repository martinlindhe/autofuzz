
class giflib:
    name = __name__
    scm = "git"
    origin = "git://git.code.sf.net/p/giflib/code"
    dataTypes = [
        "gif"
    ]

    targets = [
        "util/giftext"
    ]

    clean = [
        "make distclean"
    ]

    build = [
        "CC=afl-gcc ./autogen.sh --disable-shared",
        "make"
    ]
