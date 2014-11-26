# STATUS xxx

# dont compile on osx


class poppler:
    name = __name__
    home = "http://poppler.freedesktop.org/"
    scmOrigin = "git clone git://git.freedesktop.org/git/poppler/poppler"
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
        "./autogen.sh",
        "CC=afl-gcc ./configure --disable-shared",
        "make"
    ]
