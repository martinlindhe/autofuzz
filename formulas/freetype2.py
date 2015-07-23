# STATUS builds

# TODO fuzzable binaries are in freetype2-demos repository: git clone git://git.sv.nongnu.org/freetype/freetype2-demos.git
#  XXX the freetype2-demos need X11 display to run

class freetype2:
    name = __name__
    home = "http://www.freetype.org/"
    scmOrigin = "git clone git://git.sv.nongnu.org/freetype/freetype2.git {destination}"
    dataTypes = [
        "ttf"
    ]

    target = "xxx"
    targetParam = ""
    aflFuzzParam = ""

    clean = [
        "make distclean"
    ]

    build = [
        "./autogen.sh",
        "CC={AFL_CC} ./configure --disable-shared",
        "make"
    ]
