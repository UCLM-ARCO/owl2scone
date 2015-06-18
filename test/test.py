#!/usr/bin/python
# -*- coding: utf-8; mode: python -*-

from lxml import etree


file = "/home/tato/repos/owl2scone/test/food.rdf"
tree = etree.parse(file)
root = tree.getroot()
indv = root.findall('owl:Class', root.nsmap)
for i in indv:
    b = i.attrib
    for val in b.values():
        print val
