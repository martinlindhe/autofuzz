# STATUS builds, but needs patch to run with instrumentation

# BUG userspace/Makefile directly specifies gcc, patch sent 2014-11-17

class xzembedded:
    name = __name__
    home = "http://tukaani.org/xz/"
    scmOrigin = "git clone http://git.tukaani.org/xz-embedded.git; patch -Np1 < patches/xzembedded-001-userspace-Makefile-dont-override-CC.diff"   # XXX verify apply patch works
    dataTypes = [
        "xz"
    ]

    target = "userspace/xzminidec"
    targetParam = ""
    aflFuzzParam = ""

    clean = [
        "cd userspace; make clean"
    ]

    build = [
        "cd userspace; CC=afl-gcc make"
    ]
