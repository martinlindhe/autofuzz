# STATUS: works

# Jul 2015: xxx


class wladx:
    name = __name__
    home = "https://github.com/vhelin/wla-dx"
    scmOrigin = "git clone https://github.com/vhelin/wla-dx.git {destination}"
    dataTypes = [
        "txt"
    ]

    target = "build/binaries/wla-gb"
    targetParam = "-o"
    aflFuzzParam = ""

    clean = [
    ]

    build = [
        "mkdir build",
        "cd build && CC=afl-clang cmake -DCMAKE_BUILD_TYPE=Debug .. && make"
    ]
