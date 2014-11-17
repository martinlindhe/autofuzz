# STATUS builds, xxx need sample & target binary

class theora:
    name = __name__
    home = "http://www.theora.org/"
    scmOrigin = "https://git.xiph.org/mirrors/theora.git"
    dataTypes = [
        "theora"
    ]

    target = "examples/dump_video"     # XXX not sure its a fuzzable target
    targetParam = "-d"
    aflFuzzParam = ""

    clean = [
        "make distclean"
    ]

    build = [
        "./autogen.sh",
        "CC=afl-gcc ./configure --disable-shared",
        "make"
    ]
