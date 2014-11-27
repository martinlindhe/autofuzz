# STATUS xxx

# TODO (on osx): error: __thread support required

class elfutils:
    name = __name__
    home = "https://fedorahosted.org/elfutils/"
    scmOrigin = "git clone git://git.fedorahosted.org/git/elfutils.git {destination}"
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
        "autoreconf -fiv",
        "CC=afl-gcc ./configure",
        "make"
    ]
