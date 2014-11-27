# STATUS xxx

# XXX autogen.sh fails (osx): sed: RE error: illegal byte sequence

class gettext:
    name = __name__
    home = "https://www.gnu.org/software/gettext/"
    scmOrigin = "git clone git://git.savannah.gnu.org/gettext.git {destination}"
    dataTypes = [
        "xxx"
    ]

    target = "xxx"
    targetParam = ""
    aflFuzzParam = ""

    clean = [
        "make distclean"
    ]

    build = [
        "./autogen.sh",
        "CC=afl-gcc ./configure --disable-shared",
        "make"
    ]
