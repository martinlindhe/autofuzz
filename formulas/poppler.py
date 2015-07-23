# STATUS borked


class poppler:
    name = __name__
    home = "http://poppler.freedesktop.org/"
    scmOrigin = "git clone git://git.freedesktop.org/git/poppler/poppler {destination}"
    dataTypes = [
        "pdf"
    ]

    target = "xxx"
    targetParam = ""
    aflFuzzParam = ""

    clean = [
        "make distclean"
    ]

    build = [
        "CC={AFL_CC} CXX={AFL_CXX} ./autogen.sh --disable-shared",
        "make"
    ]
