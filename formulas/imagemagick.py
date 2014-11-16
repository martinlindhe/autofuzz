# STATUS TODO - svn repo, also fix formula!

class imagemagick:
    name = __name__
    home = "http://www.imagemagick.org/"
    # TODO stable: http://www.imagemagick.org/download/ImageMagick-6.9.0-0.tar.xz
    scmOrigin = "svn co https://subversion.imagemagick.org/subversion/ImageMagick/trunk/"
    dataTypes = [
        "bmp", "ico"
    ]

    target = "xxx"
    targetParam = ""

    clean = [
        "make distclean"
    ]

    build = [
        "./autogen.sh",
        "CC=afl-gcc ./configure --disable-shared",
        "make"
    ]
