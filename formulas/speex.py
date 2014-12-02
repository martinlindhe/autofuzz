# STATUS runs

# NOTE: uses system libogg-dev

# NOTE: on Linux, if errror Cannot open /dev/dsp: No such file or directory:
# sudo modprobe snd-pcm-oss

# Nov 2014:
#        run time : 4 days, 16 hrs, 6 min, 41 sec        cycles done : 12.6k
#   last new path : 4 days, 14 hrs, 45 min, 36 sec       total paths : 9
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
        "CC=afl-gcc ./configure --disable-shared --enable-binaries",
        "make"
    ]
