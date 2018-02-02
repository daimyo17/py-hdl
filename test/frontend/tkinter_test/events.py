from tkinter import *

class event_engine:

    eventParent = 0
    button1 = 0
    button3 = 0
    xCursor = 0
    yCursor = 0
    wheelDelta = 0


    def button1_down(self, event):
        self.button1 = 1

    def button3_down(self, event):
        self.button3 = 1

    def button1_up(self, event):
        self.button1 = 0

    def button3_up(self, event):
        self.button3 = 0

    def cursor_coord(self, event):
        self.xCursor = event.x
        self.yCursor = event.y

    def wheel_plus(self, event):
        self.wheelDelta = 3

    def wheel_minus(self, event):
        self.wheelDelta = -3

    def wheel_delta(self):
        delta = self.wheelDelta
        self.wheelDelta = 0
        return delta

    def __init__(self, eventParent):
        self.eventParent = eventParent
        self.eventParent.bind("<4>", self.wheel_minus)
        self.eventParent.bind("<5>", self.wheel_plus)
        self.eventParent.bind("<ButtonPress-1>", self.button1_down)
        self.eventParent.bind("<ButtonPress-3>", self.button3_down)
        self.eventParent.bind("<ButtonRelease-1>", self.button1_up)
        self.eventParent.bind("<ButtonRelease-3>", self.button3_up)
        self.eventParent.bind("<Motion>", self.cursor_coord)
        self.eventParent.pack()
        pass
