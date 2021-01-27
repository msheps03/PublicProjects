from Mapping_for_Tkinter import Mapping_for_Tkinter
from tkinter import *
class racket():
    def __init__(self, canvas, x, y, mapping,myracket=None): #constructor, takes canvas, x and y position, as well as mapping as arguments
        self.mapping=mapping
        self.canvas=canvas
        self.x=x
        self.y=y
        self.myracket=myracket

    def create_rectangle(self): #create the racket
        self.myracket=self.canvas.create_rectangle(self.mapping.get_i(self.x)+30,self.mapping.get_j(self.y)+5,self.mapping.get_i(self.x)-30,self.mapping.get_j(self.y)-5,fill="black")
    #methods
    def shift_left(self): #redraw rectangle 30 pixels left of where it was previously
        if self.x != -270: #check if racket is at edge, if not move it to the left 30 pixels and update x position
            self.canvas.move(self.myracket,-30,0)
            self.x-=30
        else:
            pass

    def shift_right(self): #redraw rectangle 30 pixels right of where it was previously
        if self.x != 270: #check if racket is at edge, if not move it to the right 30 pixels and update x position
            self.canvas.move(self.myracket,30,0)
            self.x+=30
        else:
            pass

    def get_xracket(self): # returns x position of the racket
        return self.x

    def get_yracket(self): # returns y position of the racket
        return self.y

    def activate(self): # turns the rectangle red when called
        self.canvas.itemconfig(self.myracket,fill="red")

    def deactivate(self): # turns rectangle black when called
        self.canvas.itemconfig(self.myracket,fill="black")

def main(): # main function
    window = Tk() # intialize TK() as window
    mapping = Mapping_for_Tkinter(-300, 300, -300, 300, 600) # initialize mapping
    canvas = Canvas(window, width=mapping.get_width(), height=mapping.get_height()) # initialize canvas
    myracket=racket(canvas, 0, -295, mapping) # bind class racket to myracket
    myracket.create_rectangle() # creates racket
    canvas.pack() # draws canvas
    canvas.bind("<Button-1>", lambda e: myracket.shift_left()) # when left mouse button is clicked move left
    canvas.bind("<Button-3>", lambda e: myracket.shift_right()) # when right mouse button is clicked move right

    window.mainloop() # wait until window is closed to proceed

if __name__=="__main__":
    main()