# STATUS works

class lodepng:
    name = __name__
    home = "http://lodev.org/lodepng/"
    scmOrigin = "git clone https://github.com/lvandeve/lodepng"
    dataTypes = [
        "png"
    ]

    target = "example_decode"
    targetParam = ""
    aflFuzzParam = "-f test.png"

    clean = [
        "rm -f example_decode"
    ]

    build = [
        "afl-gcc -x c lodepng.cpp example_decode.c -o example_decode"
    ]
