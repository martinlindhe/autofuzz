import os
import subprocess
import sys
import psutil

from distutils.version import StrictVersion


class OsxProbe:
    def RunCommand(self, command):
        # TODO move to util class
        return subprocess.check_output(
            command,
            shell=True,
            stderr=subprocess.STDOUT)

    def GetOsVersionNumber(self):
        raw = self.RunCommand("sw_vers -productVersion")
        return raw.decode('ascii').strip("\n")

    def GetApplicationVersionNumber(self, appName):
        raw = self.RunCommand("plutil -p /Applications/" + appName + ".app/Contents/Info.plist | grep 'CFBundleShortVersionString' | grep -o '\"[[:digit:].]*\"'")
        return raw.decode('ascii').strip("\"\n")

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
        if not self.IsDetected():
            print("ERROR - only OSX is supported")
            return False

        if not self.Is64Bit():
            print("ERROR - not 64bit")
            return False

        if StrictVersion(self.GetOsVersionNumber()) < StrictVersion("10.9.5"):
            print("ERROR - too old osx version")
            return False

        if StrictVersion(self.GetApplicationVersionNumber("Xcode")) < StrictVersion("5.1.1"):
            print("ERROR - Xcode is too old")
            return False

        return True

    def IsDetected(self):
        if sys.platform == "darwin":
            return True
        return False

    def GetOsVersionName(self):
        ''' @return eg "Mavericks" '''
        ver = self.GetOsVersionNumber()

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
