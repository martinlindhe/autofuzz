# STATUS xxx

class flac:
    name = __name__
    home = "http://xiph.org/flac/"
    scmOrigin = "git clone https://git.xiph.org/flac.git"
    dataTypes = [
        "flac"
    ]

    target = "xxx"
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
