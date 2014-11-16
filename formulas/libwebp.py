# STATUS broken

class libwebp:
    name = __name__
    home = "https://developers.google.com/speed/webp/"
    scmOrigin = "git clone https://chromium.googlesource.com/webm/libwebp"
    dataTypes = [
        "webp"
    ]

    targets = [
        "util/giftext"
    ]

    clean = [
        "make distclean"
    ]

    build = [
        "CC=afl-gcc ./autogen.sh --disable-shared",
        "make"
    ]
