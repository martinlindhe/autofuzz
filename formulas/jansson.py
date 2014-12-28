# STATUS builds, need sample


class jansson:
    name = __name__
    home = "http://www.digip.org/jansson/"
    scmOrigin = "git clone https://github.com/akheron/jansson {destination}"
    dataTypes = [
        "json"
    ]

    target = "test/bin/json_process"
    targetParam = ""
    aflFuzzParam = ""

    clean = [
        "make distclean"
    ]

    build = [
        "autoreconf -i",
        "./configure --disable-shared CC=afl-gcc",
        "make",
        "cd test/bin && make json_process",
    ]
