# STATUS builds, need opus sample

class opus:
    name = __name__
    home = "http://opus-codec.org/"
    scmOrigin = "git clone git://git.opus-codec.org/opus.git"
    dataTypes = [
        "opus"
    ]

    target = "opus_demo"
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
