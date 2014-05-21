#!/usr/bin/env python
"""
Python 3.x

consoleutils.py

Provides common functions for command line scripts and programs
"""
import subprocess
import sys
import time

__author__ = 'Kevin K. <kbknapp@gmail.com>'
__VERSION = '1.0'

def show_progress_bar(size, calc_dir=None, speed=None, secs=None):
    if calc_dir:
        du_cmd = 'du -c %s | grep total | awk \'{print $1}\'' % calc_dir
        du_proc = subprocess.Popen(du_cmd, shell=True, stdout=subprocess.PIPE)
        du_out, _ = du_proc.communicate()
        cycles = int(((int(du_out[:-1])/1024)/speed)*4)
    elif secs:
        cycles = secs*3
    else:
        cycles = 15
    fmt_str = '[%%-%ss] %%d%%%%' % size
    for i in range(1, cycles + 1):
        sys.stdout.write('\r')
        percent = ((i*1.0)/cycles)
        sys.stdout.write(fmt_str % ('='*int(percent*size), int(percent*100)))
        sys.stdout.flush()
        time.sleep(.45)
    print

def print_version():
    print '\nconsoleutils.py\t\tv%s\n' % __VERSION

def get_usage(args):
    usage = ''
    for k in args:
        if len(k) > 2:
            tabs = '\t'*1
        else:
            tabs = '\t'*2
        usage += '\t' + k + tabs + args[k] + '\n'
    return 'Usage: adminutils.py [flags]\n%s' % (usage)

def main(argv):
    if len(argv) == 0 or argv[0] not in args:
        return get_usage(__VALID_ARGS)
    else:
        do_args = {'-v':print_version, '--version':print_version}
        do_args[argv[0]]()

    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
