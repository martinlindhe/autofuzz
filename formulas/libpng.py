# STATUS: builds, but dont build readpng

class libpng:
    name = __name__
    home = "http://www.libpng.org/pub/png/libpng.html"
    scmOrigin = "git clone git://git.code.sf.net/p/libpng/code {destination}"
    dataTypes = [
        "png"
    ]

    target = "readpng"
    targetParam = ""
    aflFuzzParam = ""

    clean = [
        "make distclean"
    ]

    build = [
        "./autogen.sh",
        "CC=afl-gcc ./configure --disable-shared",
        "make",
        "make contrib/libtests/readpng"   # XXX not enough
    ]
