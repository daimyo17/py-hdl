from tkinter import *

class chip:
    squareHandler = 0
    tableParent = 0
    relSize = 0
    xUp = 0
    yUp = 0
    xDown = 0
    yUp = 0

    def __init__(self, tableHandler, xUp, yUp, xDown, yDown, relSize):
        self.squareHandler = tableHandler.create_rectangle(xUp, yUp, xDown, yDown, fill="#476042")
        self.tableParent = tableHandler
        self.xUp = xUp
        self.yUp = yUp
        self.xDown = xDown
        self.yDown = yDown
        self.relSize = relSize
        pass

    def update(self, xUp, yUp, xDown, yDown):
        self.tableParent.delete(self.squareHandler)
        self.squareHandler = self.tableParent.create_rectangle(xUp, yUp, xDown, yDown, fill="#476042")
        self.xUp = xUp
        self.yUp = yUp
        self.xDown = xDown
        self.yDown = yDown
        pass

    def change_size(size, relSize):
        self.relSize = relSize
        self.update(self.xUp, self.yUp, self.xDown + self.relSize, self.yDown + self.relSize)
        pass
