# STATUS xxx

# XXX osx: ./bootstrap: line 825: autopoint: command not found

class tar:
    name = __name__
    home = "https://www.gnu.org/software/tar/"
    scmOrigin = "git clone git://git.savannah.gnu.org/tar.git"
    dataTypes = [
        "tar"
    ]

    target = "xxxx"
    targetParam = ""
    aflFuzzParam = ""

    clean = [
        "make distclean"
    ]

    build = [
        "./bootstrap",
        "CC=afl-gcc ./configure --disable-shared",
        "make"
    ]
