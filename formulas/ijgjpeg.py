# STATUS no scm exists, only tarballs, need tarball support + sha1 support, also fix formula!

class ijgjpeg:
    name = "IJG jpeg"
    home = "http://www.ijg.org/"
    # TODO stable: http://www.ijg.org/files/jpegsrc.v9a.tar.gz
    scmOrigin = ""
    dataTypes = [
        "jpeg"
    ]

    target = "djpeg"
    targetParam = ""
    aflFuzzParam = ""

    clean = [
        "make distclean"
    ]

    build = [
        "autoreconf -fiv",
        "CC=afl-gcc ./configure --disable-shared",
        "make"
    ]
