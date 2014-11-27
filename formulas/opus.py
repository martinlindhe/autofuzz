# STATUS builds, need good sample?

# XXX errorr with sample, Invalid payload length: 1332176723
# NOTE trying opustools instead

class opus:
    name = __name__
    home = "http://opus-codec.org/"
    scmOrigin = "git clone git://git.opus-codec.org/opus.git {destination}"
    dataTypes = [
        "opus"
    ]

    target = "opus_demo"
    targetParam = "-d 8000 1 in.opus test.raw-from-opus"
    aflFuzzParam = "-f in.opus"

    clean = [
        "make distclean"
    ]

    build = [
        "./autogen.sh",
        "CC=afl-gcc ./configure --disable-shared",
        "make"
    ]
