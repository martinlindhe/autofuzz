# STATUS builds

# NOTE uses system libpcap-dev

# XXXX how to fuzz using pcap file?!?!?!

class tcpdump:
    name = __name__
    home = "http://www.tcpdump.org/"
    scmOrigin = "git clone https://github.com/the-tcpdump-group/tcpdump.git"
    dataTypes = [
        "pcap"
    ]

    target = "tcpdump"
    targetParam = ""
    aflFuzzParam = ""

    clean = [
        "make distclean"
    ]

    build = [
        "CC=afl-gcc ./configure --disable-shared",
        "make"
    ]
