# STATUS runs

# Nov 2014 - no problems found:
#        run time : 8 days, 2 hrs, 19 min, 59 sec        cycles done : 155
#   last new path : 1 days, 12 hrs, 19 min, 42 sec       total paths : 45
# last uniq crash : none seen yet                       uniq crashes : 0
#  last uniq hang : none seen yet                         uniq hangs : 0

class vorbis:
    name = __name__
    home = "http://wwwxxxxxx"
    scmOrigin = "https://git.xiph.org/mirrors/vorbis.git"
    dataTypes = [
        "vorbis"
    ]

    target = "examples/decoder_example"
    targetParam = ""
    aflFuzzParam = ""

    clean = [
        "make distclean"
    ]

    build = [
        "CC=afl-gcc ./autogen.sh --disable-shared",
        "make",
        "cd examples; make"
    ]
