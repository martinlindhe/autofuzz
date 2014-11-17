# STATUS xxx

class vorbis:
    name = __name__
    home = "http://wwwxxxxxx"
    scmOrigin = "https://git.xiph.org/mirrors/vorbis.git"
    dataTypes = [
        "theora"
    ]

    target = "xxx"
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
