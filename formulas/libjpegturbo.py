# STATUS works, but need jpeg input to be good!

class libjpegturbo:
    name = __name__
    home = "http://libjpeg-turbo.virtualgl.org/"
    # TODO stable: http://sourceforge.net/projects/libjpeg-turbo/files/1.3.1/libjpeg-turbo-1.3.1.tar.gz/download
    scmOrigin = "svn checkout svn://svn.code.sf.net/p/libjpeg-turbo/code/trunk"
    dataTypes = [
        "jpg"
    ]

    target = "djpeg"
    targetParam = ""

    clean = [
        "make distclean"
    ]

    build = [
        "autoreconf -fiv",
        "CC=afl-gcc ./configure --disable-shared",
        "make"
    ]
