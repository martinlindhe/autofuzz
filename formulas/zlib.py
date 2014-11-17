# STATUS works, XXX unsure if its proper, found 4 paths in ~5 minutes

class zlib:
    name = __name__
    home = "http://www.zlib.net/"
    scmOrigin = "git clone https://github.com/madler/zlib"
    dataTypes = [
        "deflate"
    ]

    target = "examples/zpipe"
    targetParam = "-d"
    aflFuzzParam = ""

    clean = [
        "make distclean"
    ]

    build = [
        "CC=afl-gcc ./configure",
        "make",
        "afl-gcc -L. libz.so examples/zpipe.c -o examples/zpipe"
    ]
