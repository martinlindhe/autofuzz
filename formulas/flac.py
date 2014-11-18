# STATUS runs - found a crasher!

# NOTE flac testcase is somewhat big, 14k

# NOTE flac binary uses shared libs even tho --disable-shared was used!?

class flac:
    name = __name__
    home = "http://xiph.org/flac/"
    scmOrigin = "git clone https://git.xiph.org/flac.git"
    dataTypes = [
        "flac"
    ]

    target = "src/flac/flac"
    targetParam = "-d -f -"   # reads from stdin, writes to stdout
    aflFuzzParam = ""

    clean = [
        "make distclean"
    ]

    build = [
        "./autogen.sh",
        "CC=afl-gcc CXX=afl-g++ ./configure --disable-shared",
        "make"
    ]
