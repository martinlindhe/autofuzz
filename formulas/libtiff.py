# STATUS xxx

# TODO cvs repository, 26 nov 2014

# export CVSROOT=:pserver:cvsanon@cvs.maptools.org:/cvs/maptools/cvsroot
# cvs login
# (use empty password)
# cvs checkout libtiff
# to get the stable libtiff code or
# cvs checkout -r branch-3-9 libtiff
# to get the previous stable branch supporting the 3.9.X release series.


class libtiff:
    name = __name__
    home = "http://www.remotesensing.org/libtiff/"
    scmOrigin = "xxx"
    dataTypes = [
        "xxx"
    ]

    target = "xxx"
    targetParam = ""
    aflFuzzParam = ""

    clean = [
        "make distclean"
    ]

    build = [
        "xxx"
    ]
