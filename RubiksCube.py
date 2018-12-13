from tkinter import *
from tkinter import ttk
from math import *
class Frame(Frame):
    def __init__(self):
        super().__init__()
        self.canvas = Canvas(self)
        self.initUI()


    def initUI(self):
        self.master.title("Lines")
        self.pack(fill=BOTH, expand=1)
        #self.canvas.create_line(15, 25, 200, 25)
        #self.canvas.create_line(300, 35, 300, 200, dash=(4, 2))

        self.cube = Cube(self)
        self.canvas.pack(fill=BOTH, expand=1)


class Cube():
    def __init__(self, frame):
        #frame.canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85)
        #frame.canvas.create_line(20, 50, 220, 25)
        #frame.canvas.create_line(100, 50, 220, 25)
        self.yTilt = 20
        self.xTilt = 90
        self.center = Point(300, 300)
        self.sidelength = 80
        self.diagnol = self.sidelength * sqrt(2)
        self.verticies = [Point(self.center.x + self.sidelength * cos(radians(self.xTilt)), self.center.y + self.sidelength * sin(radians(self.xTilt)) * sin(radians(self.yTilt))),
                          Point(self.center.x + self.sidelength * cos(radians(self.xTilt + 90)), self.center.y + self.sidelength * sin(radians(self.xTilt + 90)) * sin(radians(self.yTilt))),
                          Point(self.center.x + self.sidelength * cos(radians(self.xTilt + 180)), self.center.y + self.sidelength * sin(radians(self.xTilt + 180)) * sin(radians(self.yTilt))),
                          Point(self.center.x + self.sidelength * cos(radians(self.xTilt + 270)), self.center.y + self.sidelength * sin(radians(self.xTilt + 270)) * sin(radians(self.yTilt))),
                          Point(self.center.x + self.sidelength * cos(radians(self.xTilt)), self.sidelength + self.center.y + self.sidelength * sin(radians(self.xTilt)) * sin(radians(self.yTilt))),
                          Point(self.center.x + self.sidelength * cos(radians(self.xTilt + 90)), self.sidelength + self.center.y + self.sidelength * sin(radians(self.xTilt + 90)) * sin(radians(self.yTilt))),
                          Point(self.center.x + self.sidelength * cos(radians(self.xTilt + 180)), self.sidelength + self.center.y + self.sidelength * sin(radians(self.xTilt + 180)) * sin(radians(self.yTilt))),
                          Point(self.center.x + self.sidelength * cos(radians(self.xTilt + 270)), self.sidelength + self.center.y + self.sidelength * sin(radians(self.xTilt + 270)) * sin(radians(self.yTilt)))]
        self.edges = [frame.canvas.create_line(self.verticies[0].x, self.verticies[0].y, self.verticies[1].x, self.verticies[1].y)
                        , frame.canvas.create_line(self.verticies[1].x, self.verticies[1].y, self.verticies[2].x, self.verticies[2].y)
                        , frame.canvas.create_line(self.verticies[2].x, self.verticies[2].y, self.verticies[3].x, self.verticies[3].y)
                        , frame.canvas.create_line(self.verticies[3].x, self.verticies[3].y, self.verticies[0].x, self.verticies[0].y)
                        , frame.canvas.create_line(self.verticies[4].x, self.verticies[4].y, self.verticies[5].x, self.verticies[5].y)
                        , frame.canvas.create_line(self.verticies[5].x, self.verticies[5].y, self.verticies[6].x, self.verticies[6].y)
                        , frame.canvas.create_line(self.verticies[6].x, self.verticies[6].y, self.verticies[7].x, self.verticies[7].y)
                        , frame.canvas.create_line(self.verticies[7].x, self.verticies[7].y, self.verticies[4].x, self.verticies[4].y)]
    def redraw(self, canvas, up):
        self.verticies = [Point(self.center.x + self.sidelength * cos(radians(self.xTilt)), self.center.y + self.sidelength * sin(radians(self.xTilt)) * sin(radians(self.yTilt))),
                          Point(self.center.x + self.sidelength * cos(radians(self.xTilt + 90)), self.center.y + self.sidelength * sin(radians(self.xTilt + 90)) * sin(radians(self.yTilt))),
                          Point(self.center.x + self.sidelength * cos(radians(self.xTilt + 180)), self.center.y + self.sidelength * sin(radians(self.xTilt + 180)) * sin(radians(self.yTilt))),
                          Point(self.center.x + self.sidelength * cos(radians(self.xTilt + 270)), self.center.y + self.sidelength * sin(radians(self.xTilt + 270)) * sin(radians(self.yTilt))),
                          Point(self.center.x + self.sidelength * cos(radians(self.xTilt)), self.sidelength + self.center.y + self.sidelength * sin(radians(self.xTilt)) * sin(radians(self.yTilt))),
                          Point(self.center.x + self.sidelength * cos(radians(self.xTilt + 90)), self.sidelength + self.center.y + self.sidelength * sin(radians(self.xTilt + 90)) * sin(radians(self.yTilt))),
                          Point(self.center.x + self.sidelength * cos(radians(self.xTilt + 180)), self.sidelength + self.center.y + self.sidelength * sin(radians(self.xTilt + 180)) * sin(radians(self.yTilt))),
                          Point(self.center.x + self.sidelength * cos(radians(self.xTilt + 270)), self.sidelength + self.center.y + self.sidelength * sin(radians(self.xTilt + 270)) * sin(radians(self.yTilt)))]
        canvas.coords(self.edges[0], self.verticies[0].x, self.verticies[0].y, self.verticies[1].x, self.verticies[1].y)
        canvas.coords(self.edges[1], self.verticies[1].x, self.verticies[1].y, self.verticies[2].x, self.verticies[2].y)
        canvas.coords(self.edges[2], self.verticies[2].x, self.verticies[2].y, self.verticies[3].x, self.verticies[3].y)
        canvas.coords(self.edges[3], self.verticies[3].x, self.verticies[3].y, self.verticies[0].x, self.verticies[0].y)
        canvas.coords(self.edges[4], self.verticies[4].x, self.verticies[4].y, self.verticies[5].x, self.verticies[5].y)
        canvas.coords(self.edges[5], self.verticies[5].x, self.verticies[5].y, self.verticies[6].x, self.verticies[6].y)
        canvas.coords(self.edges[6], self.verticies[6].x, self.verticies[6].y, self.verticies[7].x, self.verticies[7].y)
        canvas.coords(self.edges[7], self.verticies[7].x, self.verticies[7].y, self.verticies[4].x, self.verticies[4].y)



    #def drawTopFace(self):
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

def left(event):
    frame.cube.xTilt = frame.cube.xTilt + 3
    frame.cube.redraw(frame.canvas, False)
    print('o')

def right(event):
    frame.cube.xTilt = frame.cube.xTilt - 3
    frame.cube.redraw(frame.canvas, False)
    print('o')

def up(event):
    frame.cube.yTilt = frame.cube.yTilt - 5
    frame.cube.redraw(frame.canvas, True)
    print('o')

def down(event):
    frame.cube.yTilt = frame.cube.yTilt + 5
    frame.cube.redraw(frame.canvas, True)
    print('o')

def bigger(event):
    frame.cube.sidelength = frame.cube.sidelength + 5
    frame.cube.redraw(frame.canvas, True)
    print('o')

def smaller(event):
    frame.cube.sidelength = frame.cube.sidelength - 5
    frame.cube.redraw(frame.canvas, True)
    print('o')

root = Tk()
frame = Frame()
root.bind('<Left>', left)
root.bind('<Right>', right)
root.bind('<Up>', up)
root.bind('<Down>', down)
root.bind('w', bigger)
root.bind('s', smaller)

root.geometry("600x600+300+300")
root.mainloop()