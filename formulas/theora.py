# STATUS builds

# XXX need sample & target binary

class theora:
    name = __name__
    home = "http://www.theora.org/"
    scmOrigin = "https://git.xiph.org/mirrors/theora.git {destination}"
    dataTypes = [
        "theora"
    ]

    target = "examples/dump_video"     # XXX not sure its a fuzzable target
    targetParam = ""
    aflFuzzParam = ""

    clean = [
        "make distclean"
    ]

    build = [
        "CC=afl-gcc ./autogen.sh --disable-shared",
        "make"
    ]
