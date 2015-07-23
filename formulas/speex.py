# STATUS runs

# NOTE: uses system libogg-dev

# NOTE: on Linux, if errror Cannot open /dev/dsp: No such file or directory:
# sudo modprobe snd-pcm-oss

# Dec 2014 - runs super slow!
#        run time : 7 days, 7 hrs, 52 min, 54 sec        cycles done : 0
#   last new path : 5 days, 4 hrs, 34 min, 37 sec        total paths : 14
# last uniq crash : none seen yet                       uniq crashes : 0
#  last uniq hang : none seen yet                         uniq hangs : 0


class speex:
    name = __name__
    home = "http://www.speex.org/"
    scmOrigin = "git clone http://git.xiph.org/speex.git {destination}"
    dataTypes = [
        "speex"
    ]

    target = "src/speexdec"
    targetParam = "-"   # stdin
    aflFuzzParam = "-t 10000"

    clean = [
        "make distclean"
    ]

    build = [
        "./autogen.sh",
        "CC={AFL_CC} ./configure --disable-shared --enable-binaries",
        "make"
    ]
