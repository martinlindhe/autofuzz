# STATUS: incomplete

class libpng:
    name = __name__
    home = "http://www.libpng.org/pub/png/libpng.html"
    scmOrigin = "git clone git://git.code.sf.net/p/libpng/code"
    dataTypes = [
        "png"
    ]

    targets = [
        "readpng"
    ]

    clean = [
        "make distclean"
    ]

    build = [
        "./autogen.sh",
        "CC=afl-gcc ./configure --disable-shared",
        "make"
    ]
