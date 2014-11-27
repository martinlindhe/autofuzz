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
        "CC=afl-gcc CXX=afl-g++ ./configure --disable-shared",
        "make"
    ]
