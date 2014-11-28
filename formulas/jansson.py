# STATUS builds, need test binary & sample


class jansson:
    name = __name__
    home = "http://www.digip.org/jansson/"
    scmOrigin = "git clone https://github.com/akheron/jansson {destination}"
    dataTypes = [
        "json"
    ]

    target = "xxx"
    targetParam = ""
    aflFuzzParam = ""

    clean = [
        "make distclean"
    ]

    build = [
        "autoreconf -i",
        "./configure CC=afl-gcc",
        "make"
    ]
