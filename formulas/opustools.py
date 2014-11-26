# STATUS runs

# NOTE this uses system libopus-dev and libflac-dev

# Nov 2014:
#        run time : 8 days, 22 hrs, 8 min, 23 sec        cycles done : 1285
#   last new path : 5 days, 12 hrs, 52 min, 40 sec       total paths : 44
# last uniq crash : none seen yet                       uniq crashes : 0
#  last uniq hang : 3 days, 15 hrs, 33 min, 0 sec         uniq hangs : 2

class opustools:
    name = __name__
    home = "http://opus-codec.org/"
    scmOrigin = "git clone git://git.opus-codec.org/opus-tools.git"
    dataTypes = [
        "opus"
    ]

    target = "opusdec"
    targetParam = "- -"  # from stdin, to stdout
    aflFuzzParam = ""

    clean = [
        "make distclean"
    ]

    build = [
        "./autogen.sh",
        "CC=afl-gcc ./configure --disable-shared",
        "make"
    ]
