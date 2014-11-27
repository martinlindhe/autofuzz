# STATUS runs

# NOTE: needs --disable-gcc-warnings to build with gcc 4.7.2/Debian


class tar:
    name = __name__
    home = "https://www.gnu.org/software/tar/"
    scmOrigin = "git clone git://git.savannah.gnu.org/tar.git"
    dataTypes = [
        "tar"
    ]

    target = "src/tar"
    targetParam = "x"
    aflFuzzParam = ""

    clean = [
        "make distclean"
    ]

    build = [
        "./bootstrap",
        "./configure CC=afl-gcc --disable-gcc-warnings",
        "make"
    ]
