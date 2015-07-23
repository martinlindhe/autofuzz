# STATUS runs


class udis86:
    name = __name__
    home = "http://udis86.sourceforge.net/"
    scmOrigin = "git clone https://github.com/vmt/udis86.git {destination}"
    dataTypes = [
        "elf"
    ]

    target = "udcli/udcli"
    targetParam = ""
    aflFuzzParam = ""

    clean = [
        "make distclean"
    ]

    build = [
        "./autogen.sh",
        "./configure --disable-shared CC={AFL_CC}",
        "make"
    ]
