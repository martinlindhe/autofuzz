# STATUS broken, minitar dont compile

class libarchive:
    name = __name__
    home = "http://libarchive.org/"
    scmOrigin = "git clone https://github.com/libarchive/libarchive {destination}"
    dataTypes = [
        "deflate"  # XXXX
    ]

    target = "examples/minitar/minitar"
    targetParam = ""
    aflFuzzParam = ""

    clean = [
        "make distclean"
    ]

    build = [
        "build/autogen.sh",
        "CC={AFL_CC} ./configure --disable-shared",
        "make",
        "{AFL_CC} -I libarchive -o examples/minitar/minitar examples/minitar/minitar.c .libs/libarchive.a -lz -lbz2"  # XXX dont compile
    ]
