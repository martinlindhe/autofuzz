# STATUS builds, xxx need sample & target binary

# XXX theres no binary usable for fuzzing

class libogg:
    name = __name__
    home = "http://xiph.org/ogg/"
    # XXXX http://downloads.xiph.org/releases/ogg/libogg-1.3.2.tar.gz
    scmOrigin = "svn co http://svn.xiph.org/trunk/ogg/"
    dataTypes = [
        "ogg"
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
