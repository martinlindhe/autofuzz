# STATUS runs

# Nov 2014:
#        run time : 9 days, 11 hrs, 22 min, 47 sec       cycles done : 318
#   last new path : 0 days, 3 hrs, 29 min, 26 sec        total paths : 370
# last uniq crash : none seen yet                       uniq crashes : 0
#  last uniq hang : 3 days, 15 hrs, 39 min, 8 sec         uniq hangs : 1


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
