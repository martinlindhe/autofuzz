# STATUS runs

class xz:
    name = __name__
    home = "http://tukaani.org/xz/"
    scmOrigin = "git clone http://git.tukaani.org/xz.git"
    dataTypes = [
        "xz"
    ]

    target = "src/xzdec/xzdec"    # TODO theres also lzmadec
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
