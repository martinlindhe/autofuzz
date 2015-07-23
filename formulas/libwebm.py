# STATUS builds

# XXX need sample, and dont know how to test it...

class libwebm:
    name = __name__
    home = "http://www.webmproject.org/code/"
    scmOrigin = "git clone https://chromium.googlesource.com/webm/libwebm {destination}"
    dataTypes = [
        "xxx"
    ]

    target = "xxx"
    targetParam = ""
    aflFuzzParam = ""

    clean = [
        "make clean"
    ]

    build = [
        "make CXX={AFL_CXX}"
    ]
