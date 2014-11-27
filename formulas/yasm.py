# STATUS runs


class yasm:
    name = __name__
    home = "http://yasm.tortall.net/"
    scmOrigin = "git clone https://github.com/yasm/yasm.git"
    dataTypes = [
        "txt"
    ]

    target = "yasm"
    targetParam = "test.asm"
    aflFuzzParam = "-f test.asm"

    clean = [
        "make distclean"
    ]

    build = [
        "CC=afl-gcc ./autogen.sh",
        "make"
    ]
