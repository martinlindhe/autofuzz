import os
import subprocess
import sys
import psutil

from distutils.version import LooseVersion, StrictVersion

# TODO move OsProbe to class lib & auto load it
# TODO detect installed Xcode version


class OsxProbe:

    def KillProcessAndChildren(proc_pid):
        # TODO move to util class
        process = psutil.Process(proc_pid)
        for proc in process.get_children(recursive=True):
            proc.kill()
        process.kill()
        return

    def GetOsxVersionNumber():
        proc = subprocess.Popen("sw_vers -productVersion", shell=True, universal_newlines=True, stdout=subprocess.PIPE)
        res = proc.stdout.read().strip("\n")
        OsxProbe.KillProcessAndChildren(proc.pid)
        return res

    def Is64Bit():
        if os.uname().machine == "x86_64":
            return True
        return False

    def IsSupported():
        ver = GetOsxVersionNumber()
        if StrictVersion(ver) >= StrictVersion("10.9.5"):
            if isDetected() and is64Bits():
                return True
        return False

    def IsDetected():
        if sys.platform == "darwin":
            return True
        return False

    def GetOsxVersionName():
        ''' @return eg "Mavericks" '''
        ver = GetOsxVersionNumber()

        if StrictVersion(ver) >= StrictVersion("10.10.0"):
            return "Yosemite"

        if StrictVersion(ver) >= StrictVersion("10.9.0"):
            return "Mavericks"

        if StrictVersion(ver) >= StrictVersion("10.8.0"):
            return "Mountain Lion"

        if StrictVersion(ver) >= StrictVersion("10.7.0"):
            return "Lion"

        if StrictVersion(ver) >= StrictVersion("10.6.0"):
            return "Snow Leopard"

        return "Unrecognized"


if not OsxProbe.IsDetected():
    print("ERROR - only OSX is supported")
    sys.exit()

if OsxProbe.GetOsxVersionNumber() != "10.9.5":
    # TODO accept multiple supported OSX versions
    print("ERROR - only OSX 10.9.5 is supported")
    sys.exit()

if not OsxProbe.Is64Bit():
    print("ERROR - not 64bit")
    sys.exit()

if not OsxProbe.IsSupported():
    print("ERROR - unsupported system")
    sys.exit()
