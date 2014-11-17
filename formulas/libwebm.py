# STATUS borked

class libwebm:
    name = __name__
    home = "http://www.webmproject.org/code/"
    scmOrigin = "git clone https://chromium.googlesource.com/webm/libwebm"
    dataTypes = [
        "xxx"
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
