# STATUS runs

# Dec 2014:
#        run time : 12 days, 21 hrs, 11 min, 33 sec      cycles done : 0
#   last new path : 0 days, 4 hrs, 51 min, 27 sec        total paths : 1733
# last uniq crash : none seen yet                       uniq crashes : 0      
#  last uniq hang : none seen yet                         uniq hangs : 0

class flac:
    name = __name__
    home = "http://xiph.org/flac/"
    scmOrigin = "git clone https://git.xiph.org/flac.git {destination}"
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
        "CC=afl-gcc CXX=afl-g++ ./configure --disable-shared --disable-doxygen-docs",
        "make"
    ]
