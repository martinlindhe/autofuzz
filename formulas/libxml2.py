# STATUS xxx

class libxml2:
    name = __name__
    home = "http://xmlsoft.org/"
    scmOrigin = "git clone git://git.gnome.org/libxml2"
    dataTypes = [
        "xml"
    ]

    target = "XXX"
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
