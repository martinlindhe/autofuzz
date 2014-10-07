import os
import subprocess
import sys
import psutil

from distutils.version import StrictVersion

# TODO move OsxProbe to class lib & auto load it
# TODO detect installed Xcode version


class OsxProbe:
    def RunCommand(self, command):
        return subprocess.check_output(
            command,
            shell=True,
            stderr=subprocess.STDOUT)

    def GetVersionNumber(self):
        raw = self.RunCommand("sw_vers -productVersion")
        return raw.decode('ascii').strip("\n")

    def KillProcessAndChildren(proc_pid):
        # TODO move to util class
        process = psutil.Process(proc_pid)
        for proc in process.get_children(recursive=True):
            proc.kill()
        process.kill()
        return

    def Is64Bit(self):
        if os.uname().machine == "x86_64":
            return True
        return False

    def IsSupported(self):
        ver = self.GetVersionNumber()
        if StrictVersion(ver) >= StrictVersion("10.9.5"):
            if self.IsDetected() and self.Is64Bit():
                return True
        return False

    def IsDetected(self):
        if sys.platform == "darwin":
            return True
        return False

    def GetVersionName(self):
        ''' @return eg "Mavericks" '''
        ver = self.GetOsxVersionNumber()

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

probe = OsxProbe()

if not probe.IsDetected():
    print("ERROR - only OSX is supported")
    sys.exit()

if probe.GetVersionNumber() != "10.9.5":
    # TODO accept multiple supported OSX versions
    print("ERROR - only OSX 10.9.5 is supported")
    sys.exit()

if not probe.Is64Bit():
    print("ERROR - not 64bit")
    sys.exit()

if not probe.IsSupported():
    print("ERROR - unsupported system")
    sys.exit()
