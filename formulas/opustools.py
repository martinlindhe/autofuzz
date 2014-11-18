# STATUS works

# NOTE this uses system libopus-dev and libflac-dev ...

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
