# STATUS builds

# NOTE flac binary uses shared libs even tho --disable-shared was used!?

class flac:
    name = __name__
    home = "http://xiph.org/flac/"
    scmOrigin = "git clone https://git.xiph.org/flac.git"
    dataTypes = [
        "flac"
    ]

    target = "src/flac/flac"
    targetParam = "-d"
    aflFuzzParam = ""

    clean = [
        "make distclean"
    ]

    build = [
        "./autogen.sh",
        "CC=afl-gcc CXX=afl-g++ ./configure --disable-shared",
        "make"
    ]
