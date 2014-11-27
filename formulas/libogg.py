# STATUS builds

# XXX need a target binary, the supplied ones is useless

class libogg:
    name = __name__
    home = "http://xiph.org/ogg/"
    scmOrigin = "git clone https://git.xiph.org/mirrors/ogg.git"
    dataTypes = [
        "ogg"
    ]

    target = ""
    targetParam = ""
    aflFuzzParam = ""

    clean = [
        "make distclean"
    ]

    build = [
        "CC=afl-gcc ./autogen.sh --disable-shared",
        "make"
    ]
