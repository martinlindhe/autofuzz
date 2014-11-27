# STATUS runs


class nasm:
    name = __name__
    home = "http://www.nasm.us/"
    scmOrigin = "git clone git://repo.or.cz/nasm.git"
    dataTypes = [
        "txt"
    ]

    target = "ndisasm"  # XXX also nasm target exists
    targetParam = "test.asm"
    aflFuzzParam = "-f test.asm"

    clean = [
        "make distclean"
    ]

    build = [
        "./autogen.sh",
        "CC=afl-gcc ./configure",
        "make"
    ]
