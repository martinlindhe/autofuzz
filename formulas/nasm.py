# STATUS builds, need sample


class nasm:
    name = __name__
    home = "http://www.nasm.us/"
    scmOrigin = "git clone git://repo.or.cz/nasm.git"
    dataTypes = [
        "xxx"
    ]

    target = "ndisasm"  # XXX also nasm target exists
    targetParam = ""
    aflFuzzParam = ""

    clean = [
        "make distclean"
    ]

    build = [
        "./autogen.sh",
        "CC=afl-gcc ./configure",
        "make"
    ]
