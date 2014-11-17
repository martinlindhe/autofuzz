# STATUS borked

class imagemagick:
    name = __name__
    home = "http://www.freetype.org/"
    scmOrigin = "git clone git://git.sv.nongnu.org/freetype/freetype2.git"
    # TODO is demos needed? git clone git://git.sv.nongnu.org/freetype/freetype2-demos.git
    dataTypes = [
        "xxxxxx"
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
