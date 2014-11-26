# STATUS runs

class libxml2:
    name = __name__
    home = "http://xmlsoft.org/"
    scmOrigin = "git clone git://git.gnome.org/libxml2"
    dataTypes = [
        "xml"
    ]

    target = "testReader"
    targetParam = "test.xml"
    aflFuzzParam = "-f test.xml"

    clean = [
        "make distclean"
    ]

    build = [
        "CC=afl-gcc ./autogen.sh --disable-shared",
        "make"
    ]
