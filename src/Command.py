#!/usr/bin/python
# -*- coding: utf-8; mode: python -*-

from abc import ABCMeta, abstractmethod


class SimpleCommand(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def execute(self):
        pass


class ConcreteCommand(SimpleCommand):

    def __init__(self, theName, theArgList):
        self.name = theName
        self.argList = theArgList

    def execute(self):
        print self.name + " " + ' '.join(self.argList)


class CompositeCommand(SimpleCommand):

    def __init__(self, theCommandList):
        self.commandList = theCommandList

    def add(self, command):
        self.commandList.append(command)

    def execute(self):
        for i in self.commandList:
            i.execute()


listA = ["{father}", "{thing}"]
listB = ["{son}", "{father}"]

a = ConcreteCommand("new-type", listA)
b = ConcreteCommand("new-type", listB)
l=[]
c = CompositeCommand(l)
c.add(a)
c.add(b)
c.execute()
