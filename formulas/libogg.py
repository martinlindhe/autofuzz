# STATUS builds

# XXX need sample & target binary

class libogg:
    name = __name__
    home = "http://xiph.org/ogg/"
    scmOrigin = "git clone https://git.xiph.org/mirrors/ogg.git"
    dataTypes = [
        "ogg"
    ]

    target = "src/test_bitwise"   # XXX dont know if it works
    targetParam = ""
    aflFuzzParam = ""

    clean = [
        "make distclean"
    ]

    build = [
        "CC=afl-gcc ./autogen.sh --disable-shared",
        "make"
    ]
