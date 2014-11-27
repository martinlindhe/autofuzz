# STATUS runs


# NOTE: uses system libogg-dev

class speex:
    name = __name__
    home = "http://www.speex.org/"
    scmOrigin = "git clone http://git.xiph.org/speex.git {destination}"
    dataTypes = [
        "speex"
    ]

    target = "src/speexdec"
    targetParam = "-"   # stdin
    aflFuzzParam = ""

    clean = [
        "make distclean"
    ]

    build = [
        "./autogen.sh",
        "CC=afl-gcc ./configure --disable-shared --enable-binaries",
        "make"
    ]
