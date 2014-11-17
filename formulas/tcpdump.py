# STATUS borked

class libwebp:
    name = __name__
    home = "http://www.tcpdump.org/"
    scmOrigin = "git clone git://bpf.tcpdump.org/tcpdump"
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
