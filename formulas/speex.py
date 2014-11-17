# STATUS builds, untested need sample

class speex:
    name = __name__
    home = "http://www.speex.org/"
    scmOrigin = "git clone http://git.xiph.org/speex.git"
    dataTypes = [
        "speex"
    ]

    target = "src/speexdec"
    targetParam = ""
    aflFuzzParam = ""

    clean = [
        "make distclean"
    ]

    build = [
        "./autogen.sh",
        "CC=afl-gcc ./configure --disable-shared --enable-binaries",
        "make"
    ]
