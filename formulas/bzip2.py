# STATUS xxxx, no scm exists ???

class bzip2:
    name = __name__
    home = "http://www.bzip.org/"
    scmOrigin = ""
## http://www.bzip.org/1.0.6/bzip2-1.0.6.tar.gz       md5 = 00b516f4704d4a7cb50a1d97e6e8e15b,   sha1 = ???, mailade bzip snubben om han kan supplya sha1 & gpg sign file
    dataTypes = [
        "bz2"
    ]

    target = "xxx"
    targetParam = ""
    aflFuzzParam = ""

    clean = [
        "make distclean"
    ]

    build = [
        "CC={AFL_CC} ./configure",
        "make"
    ]
