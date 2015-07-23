# STATUS borked

class lzo:
    name = __name__
    home = "http://www.oberhumer.com/opensource/lzo/"

    # XXX http://www.oberhumer.com/opensource/lzo/download/lzo-2.08.tar.gz
    scmOrigin = ""
    dataTypes = [
        "lzo"
    ]

    target = "xxxx"
    targetParam = ""
    aflFuzzParam = ""

    clean = [
        "make distclean"
    ]

    build = [
        "./bootstrap",
        "CC={AFL_CC} ./configure --disable-shared",
        "make"
    ]
