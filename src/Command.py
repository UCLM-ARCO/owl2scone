#!/usr/bin/python
# -*- coding: utf-8; mode: python -*-


class SimpleCommand():

    def __init__(self):
        pass

    def execute(self, commands):
        print "simple"


class ConcreteCommand(SimpleCommand):
    name = ""
    argList = []

    def __init__(self, theName, theArgList):
        self.name = theName
        self.argList = theArgList

    def execute(self):
        print "concrete"


class CompositeCommand(SimpleCommand):
    commandList = []

    def __init__(self):
        pass

    def add(self, command):
        self.commandList.append(command)
        print "add"

    def execute(self):
        for i in self.commandList:
            i.execute()

listA = ["{father}", "{thing}"]
listB = ["{son}", "{father}"]

a = ConcreteCommand("new-type", listA)
b = ConcreteCommand("new-type", listB)
c = CompositeCommand()
c.add(a)
c.add(b)
c.execute()
