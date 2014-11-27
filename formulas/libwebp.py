# STATUS runs

# Nov 2014:
#        run time : 9 days, 11 hrs, 20 min, 23 sec       cycles done : 0
#   last new path : 0 days, 0 hrs, 39 min, 51 sec        total paths : 3469
# last uniq crash : none seen yet                       uniq crashes : 0
#  last uniq hang : 9 days, 6 hrs, 2 min, 19 sec          uniq hangs : 500+

class libwebp:
    name = __name__
    home = "https://developers.google.com/speed/webp/"
    scmOrigin = "git clone https://chromium.googlesource.com/webm/libwebp {destination}"
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
