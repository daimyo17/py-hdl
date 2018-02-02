from tkinter import *
from chips import *
import time

class board:
    tableHandler = 0
    relSize = 100

    drawnChips = []

    def __init__(self, hwnd, wi, he):
        self.tableHandler = Canvas(hwnd, width=wi, height=he)
        self.tableHandler.pack()
        pass

    def new_chip(self, coordX, coordY):
        newChip = chip(self.tableHandler, coordX, coordY, coordX + self.relSize, coordY + self.relSize, self.relSize)
        self.drawnChips.append(newChip)
        pass

    def update(self, hwnd, sleep_time):
        hwnd.update_idletasks()
        hwnd.update()
        time.sleep(sleep_time)

    def chip_exist(self, coordX, coordY):
        if (len(self.drawnChips) == 0):
            return 0
        else:
            for exChip in self.drawnChips:
                if ((coordX >= exChip.xUp) and (coordX <= exChip.xDown) and (coordY >= exChip.yUp) and (coordY <= exChip.yDown)):
                    return exChip
        return 0

    def move_chip(self, exChip, coordX, coordY):
        (upLeftSide, downLeftSide) = (self.chip_exist(exChip.xUp - 15, exChip.yUp), self.chip_exist(exChip.xUp - 15, exChip.yDown))
        (upRightSide, downRightSide) = (self.chip_exist(exChip.xDown + 15, exChip.yUp), self.chip_exist(exChip.xDown + 15, exChip.yDown))
        (leftUpSide, rightUpSide) = (self.chip_exist(exChip.xUp, exChip.yUp - 15), self.chip_exist(exChip.xDown, exChip.yUp - 15))
        (leftDownSide, rightDownSide) = (self.chip_exist(exChip.xUp, exChip.yDown + 15), self.chip_exist(exChip.xDown, exChip.yDown + 15))

        if (((upLeftSide != 0) or (downLeftSide != 0)) and (upLeftSide != exChip) and (downLeftSide != exChip) and (coordX < exChip.xUp)):
            exChip.update(exChip.xUp , coordY, exChip.xDown, coordY + exChip.relSize)
        elif (((upRightSide != 0) or (downRightSide != 0)) and (upRightSide != exChip) and (downRightSide != exChip) and (coordX > exChip.xUp)):
            exChip.update(exChip.xUp , coordY, exChip.xDown, coordY + exChip.relSize)
        elif (((leftUpSide != 0) or (rightUpSide != 0)) and (leftUpSide != exChip) and (downRightSide != exChip) and (coordY < exChip.yUp)):
            exChip.update(coordX , exChip.yUp , coordX + exChip.relSize, exChip.yDown)
        elif (((leftDownSide != 0) or (rightDownSide != 0)) and (leftDownSide != exChip) and (rightDownSide != exChip) and (coordY > exChip.yUp)):
            exChip.update(coordX , exChip.yUp , coordX + exChip.relSize, exChip.yDown)
        else:
            exChip.update(coordX , coordY, coordX + exChip.relSize, coordY + exChip.relSize)

    def change_chip_size(self, exChip, relSize):
        exChip.change_size(exChip.relSize + relSize)

    def change_all_chip_sizes(self, relSize):
        for exChip in self.drawnChips:
            self.change_chip_size(exChip, relSize)
