# STATUS builds, need input files


class yasm:
    name = __name__
    home = "http://yasm.tortall.net/"
    scmOrigin = "git clone https://github.com/yasm/yasm.git"
    dataTypes = [
        "xxx"
    ]

    target = "yasm"
    targetParam = ""
    aflFuzzParam = ""

    clean = [
        "make distclean"
    ]

    build = [
        "CC=afl-gcc ./autogen.sh",
        "make"
    ]
