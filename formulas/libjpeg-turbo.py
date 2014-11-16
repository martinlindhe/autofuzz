# STATUS borked, need release / svn dl

class lodepng:
    name = __name__
    home = "http://libjpeg-turbo.virtualgl.org/"
    # TODO stable: http://sourceforge.net/projects/libjpeg-turbo/files/1.3.1/libjpeg-turbo-1.3.1.tar.gz/download
    scmOrigin = "svn checkout svn://svn.code.sf.net/p/libjpeg-turbo/code/trunk"
    dataTypes = [
        "png"
    ]

    target = "xxx"
    targetParam = ""

    clean = [
        "rm -f example_decode"
    ]

    build = [
        "afl-gcc -x c lodepng.cpp example_decode.c -o example_decode"
    ]
