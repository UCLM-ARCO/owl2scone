#!/usr/bin/python
# -*- coding: utf-8; mode: python -*-

import sys
import os.path
import xml.etree.elementTree as ET
import urllib


origin = sys.argv[1]
origin = "../test/wine.owl.rdf"
# destiny = sys.argv[2]

tree = ET.parse(origin)


def download(url):

    file_name = url.split('/')[-1] + ".rdf"
    u = urllib.urlopen(url)
    f = open(file_name, 'wb')
    meta = u.info()
    file_size = int(meta.getheaders("Content-Length")[0])
    print "Downloading: %s Bytes: %s" % (file_name, file_size)

    file_size_dl = 0
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break

        file_size_dl += len(buffer)
        f.write(buffer)
        status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
        status = status + chr(8)*(len(status)+1)
        print status,

    f.close()


def checkFiles(origin, destiny):

    if len(sys.argv) != 3:
        print "Missing files!"
    else:
        if os.path.exists(origin) and os.path.isfile(origin):
            print "Oops!, this is awkward, one of the files is not actually a file ;)"

# checkFiles(origin, destiny)
# file = open(destiny, 'w+')
