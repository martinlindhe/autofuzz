# STATUS builds, no target to fuzz

class rtmpdump:
    name = __name__
    home = "https://rtmpdump.mplayerhq.hu/"
    scmOrigin = "git clone git://git.ffmpeg.org/rtmpdump"
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
        "make SYS=darwin CC=afl-gcc"   ### XXXX SYS=posix on Linux! !!!
    ]
