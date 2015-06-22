#!/usr/bin/python
# -*- coding: utf-8; mode: python -*-

from lxml import etree


file = "/home/tato/repos/owl2scone/test/food.rdf"
#file = "/home/tato/repos/owl2scone/test/food-test.rdf"
tree = etree.parse(file)
root = tree.getroot()
indv = root.findall('owl:Class', root.nsmap)


class ConcreteCommand():
    def __init__(self, theKeyValue, theFather):
        self.keyValue = theKeyValue
        self.father = theFather

    def execute(self):
        print "new-type {" + self.keyValue + "}" + "{" + self.father + "}"


def getValues(nodeList):
    attrib = nodeList.attrib
    for v in attrib.values():
        value = v

    return value


def isRoot(node):
    children_list = node.getchildren()

    if not children_list:
        for ancestors in node.iterancestors():
            if ancestors.tag == root.tag:
                return True
    else:
        return False


def locateChildrenThing(root):
    for i in root:
        children_list = i.getchildren()
        if not children_list:
            value = getValues(i)

            print "new-type {" + value + "} {Thing}"

locateChildrenThing(indv)

# for i in indv:
#     locateChildrenThing(i)

    # children_list = i.getchildren()
    # if children_list:
    #     print children_list
    #     for child in children_list:
    #         tag = child.tag
    #         print "tag-> ", tag

    #     print "--"
