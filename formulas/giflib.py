
class giflib(object):
    name = __name__
    scm = "git"
    origin = "git://git.code.sf.net/p/giflib/code"

    build = [
        "CC=afl-gcc ./autogen.sh --disable-shared",
        "make"
    ]

    target = "util/giftext"


#    tried using util/giftext

#    afl-fuzz -i afl-0.45b/testcases/images/gif/ -o afl-out-giflib util/giftext
