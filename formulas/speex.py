# STATUS builds, xxx need sample & target binary

class theora:
    name = __name__
    home = "http://www.speex.org/"
    scmOrigin = "git clone http://git.xiph.org/speex.git"
    dataTypes = [
        "speex"
    ]

    target = "xxx"
    targetParam = ""
    aflFuzzParam = ""

    clean = [
        "make distclean"
    ]

    build = [
        "./autogen.sh",
        "CC=afl-gcc ./configure --disable-shared",
        "make"
    ]
