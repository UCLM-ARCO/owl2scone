#!/usr/bin/python
# -*- coding: utf-8; mode: python -*-

from lxml import etree


file = "/home/tato/repos/owl2scone/test/food.rdf"
tree = etree.parse(file)
root = tree.getroot()
indv = root.findall('owl:Class', root.nsmap)


def getValues(nodeList):
    attrib = nodeList.attrib
    for v in attrib.values():
        value = v

    return value


for i in indv:
    children_list = i.getchildren()
    if not children_list:
        value = getValues(i)
        print "new-type {" + value + "} {Thing}"
