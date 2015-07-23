# STATUS builds

# XXX need sample

class libvpx:
    name = __name__
    home = "http://www.webmproject.org/code/"
    scmOrigin = "git clone https://chromium.googlesource.com/webm/libvpx {destination}"
    dataTypes = [
        "xxx"
    ]

    target = "vpxdec"
    targetParam = ""
    aflFuzzParam = ""

    clean = [
        "make distclean"
    ]

    build = [
        "CC={AFL_CC} CXX={AFL_CXX} ./configure --disable-shared",
        "make"
    ]
