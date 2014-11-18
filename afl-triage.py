#!/usr/bin/env python

# NOTE this is similar to afl-0.45b/experimental/crash_triage/triage_crashes.sh

# TODO abort if Q or ESC is pressed
# TODO own git repo

import os
import sys
import argparse
import subprocess


def run_command(command):
    try:
        res = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError as e:
        print("command returned error code " + str(e.returncode))
        res = e.output

    return res

versionString = "afl-triage 0.1 (c) Martin Lindhe 2014"


parser = argparse.ArgumentParser(description='Lookup subdomains of given domain(s)')
parser.add_argument('-V', '--version', action='version',
                    version=versionString)
parser.add_argument('--dir', required=True, help='output directory from afl run')

parser.add_argument('--executable', required=True, help='afl-instrumented binary')
parser.add_argument('--stats', help='show stats', action='store_true')


args = parser.parse_args()

print(versionString)
print("")

showStats = args.stats

execFile = args.executable

fileSet = set()

# TODO make sure inDir is a afl dir, expect to find subdir "crashes", "hangs" and "queue"
crashDir = args.dir + "/crashes"

for dir_, _, files in os.walk(crashDir):
    for fileName in files:
        # skip files beginning with .
        if (fileName[0] == "."):
            continue

        if (fileName in ("fuzz_bitmap", "fuzzer_stats", "README.txt")):
            continue

        relDir = os.path.relpath(dir_, crashDir)
        relFile = os.path.join(relDir, fileName)
        fileSet.add(relFile)
        break

# TODO figure out if its a 64bit binary or not

if showStats:
    print("### stats")
    print("number of files: " + str(len(fileSet)))
    sys.exit()

for f in fileSet:
    fullFile = crashDir + "/" + f
    print(fullFile)

    # XXX: 32bit disasm:   --ex "disass $eip, $eip+16"
    disasm = '--ex "disass \$rip, \$rip+16"'
    disasm = ''
    regdump = '--ex "info reg"'
    regdump = ''
    cmd = 'gdb --batch -q -ex "r <' + fullFile + '" --ex "back" ' + disasm + ' ' + regdump + ' --ex "quit" "' + execFile + '"'
    out = run_command(cmd)
    print(cmd)

    s1 = "Program received signal"
    s2 = "A debugging session is active."
    start = out.find(s1)
    end = out.find(s2, start)

    # HACK fragile way to get only crash signature & backtrace
    stripped = out[start:end]
#    print("### stripped")
    print(stripped)
#    break

# TODO only check one file from each subdir, since they have the same "crash signature" (???)
# TODO extract crash signal & hash from path


#  sig=`basename -- "$crash_dir" | cut -d, -f1 | cut -d: -f2`
#  hash=`basename -- "$crash_dir" | cut -d, -f2 | cut -d: -f2`
#  count=`ls -- "$crash_dir" | wc -l`

#  echo "+++ HASH $hash, SIGNAL $sig ($count samples) +++"
#  echo

#  first=`ls -- "$crash_dir" |  head -1`

#  gdb --batch -q --ex "r <$crash_dir/$first" --ex 'back' --ex 'disass $eip, $eip+16' --ex 'info reg' --ex 'quit' "$BIN"
