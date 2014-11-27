# STATUS builds, need test file

class patch:
    name = __name__
    home = "https://savannah.gnu.org/projects/patch/"
    scmOrigin = "git clone git://git.savannah.gnu.org/patch.git {destination}"
    dataTypes = [
        "txt"
    ]

    target = "src/patch"
    targetParam = ""
    aflFuzzParam = ""

    clean = [
        "make distclean"
    ]

    build = [
        "./bootstrap",
        "CC=afl-gcc ./configure",
        "make"
    ]
