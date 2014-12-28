# STATUS runs

# Dec 2014:
#        run time : 12 days, 0 hrs, 2 min, 42 sec        cycles done : 0
#   last new path : 0 days, 8 hrs, 41 min, 53 sec        total paths : 1687
# last uniq crash : 2 days, 6 hrs, 38 min, 47 sec       uniq crashes : 168
#  last uniq hang : 0 days, 20 hrs, 31 min, 49 sec        uniq hangs : 7


class nasm:
    name = __name__
    home = "http://www.nasm.us/"
    scmOrigin = "git clone git://repo.or.cz/nasm.git {destination}"
    dataTypes = [
        "txt"
    ]

    target = "ndisasm"  # XXX also nasm target exists
    targetParam = "test.asm"
    aflFuzzParam = "-f test.asm"

    clean = [
        "make distclean"
    ]

    build = [
        "./autogen.sh",
        "CC=afl-gcc ./configure",
        "make"
    ]
