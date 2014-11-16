# STATUS formula works, but binary crashes afl 0.48b (reported) - need afl-fuzz "-f test.png" param for this!

class lodepng:
    name = __name__
    home = "http://lodev.org/lodepng/"
    scmOrigin = "git clone https://github.com/lvandeve/lodepng"
    dataTypes = [
        "png"
    ]

    target = "example_decode"
    targetParam = ""

    clean = [
        "rm -f example_decode"
    ]

    build = [
        "afl-gcc -x c lodepng.cpp example_decode.c -o example_decode"
    ]
