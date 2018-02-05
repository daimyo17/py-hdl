from tkinter import *
from chips import *

class port:
    portNumber = 0
    parent = 0
    chipSide = 0
    portType = 0
    portHandler = 0
    sidePortsNumber = 0
    coordX = 0
    coordY = 0

    def __init__(self, parent, portNumber, chipSide, portType, sidePortsNumber):
        self.parent = parent
        self.portNumber = portNumber
        self.chipSide = chipSide
        self.portType = portType
        self.sidePortsNumber = sidePortsNumber
        self.find_coords()
        self.portHandler = parent.tableParent.create_oval(self.coordX, self.coordY, self.coordX + 10, self.coordY + 10, fill="#000000")
        pass

    def update(self):
        self.find_coords()
        self.parent.tableParent.delete(self.portHandler)
        self.portHandler = self.parent.tableParent.create_oval(self.coordX, self.coordY, self.coordX + 10, self.coordY + 10, fill="#000000")
        pass

    def find_coords(self):
        if (self.chipSide == "left"):
            self.coordX = self.parent.xUp - 5
            self.coordY = self.parent.yUp + ((self.parent.yDown - self.parent.yUp) / self.sidePortsNumber * self.portNumber) - 5
        elif (self.chipSide == "right"):
            self.coordX = self.parent.xDown - 5
            self.coordY = self.parent.yUp + ((self.parent.yDown - self.parent.yUp) / self.sidePortsNumber * self.portNumber) - 5
        elif (self.chipSide == "up"):
            self.coordX = self.parent.xUp + ((self.parent.xDown - self.parent.xUp) / self.sidePortsNumber * self.portNumber) - 5
            self.coordY = self.parent.yUp - 5
        elif (self.chipSide == "down"):
            self.coordX = self.parent.xUp + ((self.parent.xDown - self.parent.xUp) / self.sidePortsNumber * self.portNumber) - 5
            self.coordY = self.parent.yUp - 5
