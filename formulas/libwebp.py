# STATUS runs, but needs to supply a webp test case for better fuzzing!

class libwebp:
    name = __name__
    home = "https://developers.google.com/speed/webp/"
    scmOrigin = "git clone https://chromium.googlesource.com/webm/libwebp"
    dataTypes = [
        "webp"
    ]

    target = "examples/dwebp"
    targetParam = "-- -"

    clean = [
        "make distclean"
    ]

    build = [
        "./autogen.sh",
        "CC=afl-gcc ./configure --disable-shared",
        "make"
    ]
