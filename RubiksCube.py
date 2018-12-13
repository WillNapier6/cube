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
        self.xTilt = 0
        self.center = Point(300, 300)
        self.sidelength = 120
        self.diagnol = self.sidelength * sqrt(2)
        self.updateVertices()
        self.faces = [Face(self.vertices[0:8], frame.canvas, 'green'), Face(self.vertices[8:16], frame.canvas, 'blue'), Face(self.vertices[0:2] + self.vertices[2:4] + self.vertices[10:12] + self.vertices[8:10], frame.canvas, 'yellow'),
                      Face(self.vertices[2:6] + self.vertices[12:14] + self.vertices[10:12], frame.canvas, 'orange'),  Face(self.vertices[4:8] + self.vertices[14:16] + self.vertices[12:14], frame.canvas, 'purple'), Face(self.vertices[6:8] + self.vertices[14:16] + self.vertices[8:10] + self.vertices[0:2], frame.canvas, 'pink')]
    def redraw(self, canvas, up):
        self.updateVertices()
        self.updateFaces()

    def updateVertices(self):
        self.vertices = [self.center.x + self.sidelength * cos(radians(self.xTilt)), self.center.y + self.sidelength * sin(radians(self.xTilt)) * sin(radians(self.yTilt)),
                         self.center.x + self.sidelength * cos(radians(self.xTilt + 90)), self.center.y + self.sidelength * sin(radians(self.xTilt + 90)) * sin(radians(self.yTilt)),
                         self.center.x + self.sidelength * cos(radians(self.xTilt + 180)), self.center.y + self.sidelength * sin(radians(self.xTilt + 180)) * sin(radians(self.yTilt)),
                         self.center.x + self.sidelength * cos(radians(self.xTilt + 270)), self.center.y + self.sidelength * sin(radians(self.xTilt + 270)) * sin(radians(self.yTilt)),
                         self.center.x + self.sidelength * cos(radians(self.xTilt)), self.diagnol * cos(radians(self.yTilt)) + self.center.y + self.sidelength * sin(radians(self.xTilt)) * sin(radians(self.yTilt)),
                         self.center.x + self.sidelength * cos(radians(self.xTilt + 90)), self.diagnol * cos(radians(self.yTilt))+ self.center.y + self.sidelength * sin(radians(self.xTilt + 90)) * sin(radians(self.yTilt)),
                         self.center.x + self.sidelength * cos(radians(self.xTilt + 180)), self.diagnol * cos(radians(self.yTilt))+ self.center.y + self.sidelength * sin(radians(self.xTilt + 180)) * sin(radians(self.yTilt)),
                         self.center.x + self.sidelength * cos(radians(self.xTilt + 270)), self.diagnol * cos(radians(self.yTilt))+ self.center.y + self.sidelength * sin(radians(self.xTilt + 270)) * sin(radians(self.yTilt))]
    def updateFaces(self):
        self.faces[0].vertices = self.vertices[0:8]
        self.faces[1].vertices = self.vertices[8:16]
        self.faces[2].vertices = self.vertices[0:2] + self.vertices[2:4] + self.vertices[10:12] + self.vertices[8:10]
        self.faces[3].vertices = self.vertices[2:6] + self.vertices[12:14] + self.vertices[10:12]
        self.faces[4].vertices = self.vertices[4:8] + self.vertices[14:16] + self.vertices[12:14]
        self.faces[5].vertices = self.vertices[6:8] + self.vertices[14:16] + self.vertices[8:10] + self.vertices[0:2]
        if self.yTilt%360 <= 90 and self.yTilt%360 > 0 :
            self.faces[0].canvas.itemconfigure(self.faces[0].shape, state='normal')
            self.faces[0].draw()
            self.faces[1].canvas.itemconfigure(self.faces[1].shape, state='hidden')
        else :
            self.faces[1].canvas.itemconfigure(self.faces[1].shape, state='normal')
            self.faces[1].draw()
            self.faces[0].canvas.itemconfigure(self.faces[0].shape, state='hidden')

        if (self.xTilt%360 > 0 and self.xTilt%360 <= 45) or self.xTilt%360 < 359 and self.xTilt%360 >= 315:
            self.faces[2].draw()
            self.faces[3].draw()
            self.faces[4].canvas.itemconfigure(self.faces[4].shape,  state='hidden')
            self.faces[5].canvas.itemconfigure(self.faces[5].shape, state='hidden')

class Face():
    def __init__(self, vertices, canvas, color):
        self.vertices = vertices
        self.shape = canvas.create_polygon(vertices, fill= color, width=2)
        self.canvas = canvas
    def draw(self):
        self.canvas.coords(self.shape, self.vertices)

    #def drawTopFace(self):
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

def left(event):
    frame.cube.xTilt = frame.cube.xTilt + 3
    frame.cube.redraw(frame.canvas, False)
    print(frame.cube.xTilt%360)

def right(event):
    frame.cube.xTilt = frame.cube.xTilt - 3
    frame.cube.redraw(frame.canvas, False)
    print(frame.cube.xTilt%360)

def up(event):
    if frame.cube.yTilt > -90 :
        frame.cube.yTilt = frame.cube.yTilt - 5
        frame.cube.redraw(frame.canvas, True)
        print(frame.cube.yTilt)

def down(event):
    if frame.cube.yTilt < 90:
        frame.cube.yTilt = frame.cube.yTilt + 5
        frame.cube.redraw(frame.canvas, True)
        print(frame.cube.yTilt)

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