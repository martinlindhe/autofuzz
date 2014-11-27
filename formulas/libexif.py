# STATUS borked, problems with the cvs checkout


class libexif:
    name = __name__
    home = "http://libexif.sourceforge.net/"
    scmOrigin = "cvs -d :pserver:anonymous:@libexif.cvs.sourceforge.net:/cvsroot/libexif login && cvs -z3 -d :pserver:anonymous:@libexif.cvs.sourceforge.net:/cvsroot/libexif co -d {destination} -P libexif"

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
