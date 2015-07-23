# STATUS builds

# XXX need a target binary, the supplied ones is useless

class libogg:
    name = __name__
    home = "http://xiph.org/ogg/"
    scmOrigin = "git clone https://git.xiph.org/mirrors/ogg.git {destination}"
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
        "CC={AFL_CC} ./autogen.sh --disable-shared",
        "make"
    ]
