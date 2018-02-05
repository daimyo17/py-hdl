from tkinter import *
from ports import *

class chip:
    squareHandler = 0
    tableParent = 0
    relSize = 0
    portMap = {}
    mappedPorts = []
    xUp = 0
    yUp = 0
    xDown = 0
    yUp = 0

    def __init__(self, tableHandler, xUp, yUp, xDown, yDown, relSize, portMap):
        self.xUp = xUp
        self.yUp = yUp
        self.xDown = xDown
        self.yDown = yDown
        self.relSize = relSize
        self.portMap = portMap
        self.squareHandler = tableHandler.create_rectangle(xUp, yUp, xDown, yDown, fill="#476042")
        self.tableParent = tableHandler
        self.create_ports()
        pass

    def update(self, xUp, yUp, xDown, yDown):
        self.xUp = xUp
        self.yUp = yUp
        self.xDown = xDown
        self.yDown = yDown
        self.tableParent.delete(self.squareHandler)
        self.squareHandler = self.tableParent.create_rectangle(xUp, yUp, xDown, yDown, fill="#476042")
        self.update_ports()
        pass

    def change_size(self, relSize):
        self.relSize = relSize
        self.update(self.xUp, self.yUp, self.xUp + self.relSize, self.yUp + self.relSize)
        pass

    def create_ports(self):
        for side in self.portMap.keys():
            for portType in self.portMap[side].keys():
                for index in range(1, self.portMap[side][portType] + 1):
                    self.mappedPorts.append(port(self, index, side, portType, self.portMap[side]['in'] + self.portMap[side]['out'] + 1))
        pass

    def update_ports(self):
        for dPort in self.mappedPorts:
            dPort.update()
