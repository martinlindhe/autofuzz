# STATUS borked

# XXX wont build, seems v8 files are assumed to be in path...

#Updating projects from gyp files...
#gyp: /home/ml/dev/autofuzz/.cache/pdfium/v8/tools/gyp/v8.gyp not found (cwd: /home/ml/dev/autofuzz/.cache/pdfium) while loading dependencies of /home/ml/dev/autofuzz/.cache/pdfium/pdfium.gyp while loading dependencies of /home/ml/dev/autofuzz/.cache/pdfium/samples/samples.gyp while loading dependencies of /home/ml/dev/autofuzz/.cache/pdfium/build/all.gyp while trying to load /home/ml/dev/autofuzz/.cache/pdfium/build/all.gyp
#Error running GYP

# XX more is needed:
#$  git clone https://pdfium.googlesource.com/pdfium.git
#$ cd pdfium/
#$ svn co http://gyp.googlecode.com/svn/trunk build/gyp
#$ svn co http://v8.googlecode.com/svn/trunk v8
#$ svn co https://src.chromium.org/chrome/trunk/deps/third_party/icu46 v8/third_party/icu
#$ build/gyp_pdfium
#$ make 
#$ make BUILDTYPE=Release

# from : https://code.google.com/p/pdfium/wiki/Build


class pdfium:
    name = __name__
    home = "https://code.google.com/p/pdfium/"
    scmOrigin = "git clone https://pdfium.googlesource.com/pdfium"
    dataTypes = [
        "pdf"
    ]

    target = "xxx"
    targetParam = ""
    aflFuzzParam = ""

    clean = [
        "make clean"
    ]

    build = [
        "CC=afl-gcc CXX=afl-g++ build/gyp_pdfium",
        "make pdfium_test"
    ]
