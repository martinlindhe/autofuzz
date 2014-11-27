# STATUS xxx

# TODO osx: gettext is not available, build fails

class gnupg:
    name = __name__
    home = "https://gnupg.org/"
    scmOrigin = "git clone git://git.gnupg.org/gnupg.git {destination}"
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
