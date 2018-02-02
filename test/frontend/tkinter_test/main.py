from tkinter import *
from table import board
from events import event_engine
from chips import chip

hwnd = Tk()
projectBoard = board(hwnd, 1000, 1000)
boardEvents = event_engine(projectBoard.tableHandler)

while True:
    #Create new Chip
    if ((boardEvents.button3 != 0) and (projectBoard.chip_exist(boardEvents.xCursor, boardEvents.yCursor) == 0)):
        projectBoard.new_chip(boardEvents.xCursor, boardEvents.yCursor)
        projectBoard.update(hwnd, 0.3)

    #Move existing Chip
    if ((boardEvents.button1 != 0) and (projectBoard.chip_exist(boardEvents.xCursor, boardEvents.yCursor) != 0)):
        exChip = projectBoard.chip_exist(boardEvents.xCursor, boardEvents.yCursor)
        relCoordX = boardEvents.xCursor - exChip.xUp
        relCoordY = boardEvents.yCursor - exChip.yUp
        while (boardEvents.button1 != 0):
            projectBoard.move_chip(exChip, boardEvents.xCursor - relCoordX, boardEvents.yCursor - relCoordY)
            projectBoard.update(hwnd, 0)

    #Change chip size
    if (boardEvents.wheelDelta != 0):
        exChip = projectBoard.chip_exist(boardEvents.xCursor, boardEvents.yCursor)
        if (exChip == 0):
            projectBoard.change_all_chip_sizes(boardEvents.wheel_delta())
        else:
            projectBoard.change_chip_size(exChip, boardEvents.wheel_delta())
        projectBoard.update(hwnd, 0)

    projectBoard.update(hwnd, 0)
mainloop()
