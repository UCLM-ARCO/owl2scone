#!/usr/bin/python
# -*- coding: utf-8; mode: python -*-

import sys
import os.path

origin = sys.argv[1]
destiny = sys.argv[2]


def checkFiles(origin, destiny):

    if len(sys.argv) != 3:
        print "Missing files!"
    else:
        if os.path.exists(origin) and os.path.isfile(origin):
            print "Oops!, this is awkward, one of the files is not actually a file ;)"

# checkFiles(origin, destiny)

file = open(destiny, 'w+')
