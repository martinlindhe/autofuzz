# STATUS works

class libwebp:
    name = __name__
    home = "https://developers.google.com/speed/webp/"
    scmOrigin = "git clone https://chromium.googlesource.com/webm/libwebp"
    dataTypes = [
        "webp"
    ]

    target = "examples/dwebp"
    targetParam = "-- -"
    aflFuzzParam = ""

    clean = [
        "make distclean"
    ]

    build = [
        "./autogen.sh",
        "CC=afl-gcc ./configure --disable-shared",
        "make"
    ]
