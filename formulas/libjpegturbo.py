# STATUS works

class libjpegturbo:
    name = "libjpeg-turbo"
    home = "http://libjpeg-turbo.virtualgl.org/"
    # TODO stable: http://sourceforge.net/projects/libjpeg-turbo/files/1.3.1/libjpeg-turbo-1.3.1.tar.gz/download
    scmOrigin = "svn checkout svn://svn.code.sf.net/p/libjpeg-turbo/code/trunk"
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
