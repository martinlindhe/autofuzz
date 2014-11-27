# STATUS xxx

# TODO (on osx): error: __thread support required

class elfutils:
    name = __name__
    home = "https://fedorahosted.org/elfutils/"
    scmOrigin = "git clone git://git.fedorahosted.org/git/elfutils.git {destination}"
    dataTypes = [
        "elf"
    ]

    target = "src/elflint"
    targetParam = ""
    aflFuzzParam = ""

    clean = [
        "make distclean"
    ]

    build = [
        "autoreconf -fiv",
        "CC=afl-gcc ./configure --enable-maintainer-mode",
        "make"
    ]
