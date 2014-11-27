# STATUS builds, but dont build "convert" tool ???

class imagemagick:
    name = __name__
    home = "http://www.imagemagick.org/"
    scmOrigin = "svn co https://subversion.imagemagick.org/subversion/ImageMagick/trunk/ {destination}"
    dataTypes = [
        "bmp", "ico"  # XXX care of mutliple types
    ]

    target = "utilities/magick"
    targetParam = ""
    aflFuzzParam = ""

    clean = [
        "make distclean"
    ]

    build = [
        "CC=afl-gcc CXX=afl-g++ ./configure --disable-shared --enable-delegate-build --with-modules=yes",
        "make"
    ]
