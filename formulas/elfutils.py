# STATUS runs

# Dec 2014:
#        run time : 11 days, 21 hrs, 17 min, 30 sec      cycles done : 0      
#   last new path : 0 days, 0 hrs, 28 min, 38 sec        total paths : 2773   
# last uniq crash : 0 days, 0 hrs, 29 min, 37 sec       uniq crashes : 515
#  last uniq hang : 0 days, 3 hrs, 13 min, 31 sec         uniq hangs : 383

class elfutils:
    name = __name__
    home = "https://fedorahosted.org/elfutils/"
    scmOrigin = "git clone git://git.fedorahosted.org/git/elfutils.git {destination}"
    dataTypes = [
        "elf"
    ]

    target = "src/elflint"
    targetParam = "test.elf"
    aflFuzzParam = "-f test.elf"

    clean = [
        "make distclean"
    ]

    build = [
        "autoreconf -fiv",
        "CC=afl-gcc ./configure --enable-maintainer-mode",
        "make"
    ]
