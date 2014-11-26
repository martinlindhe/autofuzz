# STATUS runs

# NOTE flac testcase is somewhat big, 14k

# NOTE flac binary uses shared libs even tho --disable-shared was used!?

# Nov 2014:
#        run time : 8 days, 3 hrs, 15 min, 41 sec      │  cycles done : 0
#   last new path : 0 days, 0 hrs, 3 min, 11 sec       │  total paths : 1237
# last uniq crash : 0 days, 9 hrs, 51 min, 38 sec      │ uniq crashes : 251
#  last uniq hang : 3 days, 15 hrs, 41 min, 19 sec     │   uniq hangs : 2


class flac:
    name = __name__
    home = "http://xiph.org/flac/"
    scmOrigin = "git clone https://git.xiph.org/flac.git"
    dataTypes = [
        "flac"
    ]

    target = "src/flac/flac"
    targetParam = "-d -f -"   # reads from stdin, writes to stdout
    aflFuzzParam = ""

    clean = [
        "make distclean"
    ]

    build = [
        "./autogen.sh",
        "CC=afl-gcc CXX=afl-g++ ./configure --disable-shared",
        "make"
    ]
