# STATUS runs

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
