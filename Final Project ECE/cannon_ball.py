from Mapping_for_Tkinter import Mapping_for_Tkinter
import time
import math
from tkinter import *

class cannon_ball:
    def __init__(self,theta,strength,v=70,cannonBall=None): # constructor for class cannon_ball
        self.theta=float(theta)*math.pi/180 # initialize theta as radians from degrees
        self.strength=float(strength)
        self.v=float(v)
        self.x0=0
        self.y0=float(mapping.get_ymin()+4) # y coordinate as bottom of window +4
        self.x=0
        self.y=float(mapping.get_ymin()+4) # y coordinate as bottom of window +4
        self.cannonBall=cannonBall

    def create_oval(self, color="blue"): # method to create the cannon ball
        self.cannonBall =canvas.create_oval(mapping.get_i(self.x) + 4, mapping.get_j(self.y) + 4,mapping.get_i(self.x) - 4, mapping.get_j(self.y) - 4,fill=color)

    def bounce(self): # method called when the ball bounces
        self.x0 = self.x
        self.v=self.v*self.strength

    def update_xy(self,t): # method that updates the x and y position of the ball
        self.x = self.x0 + self.v * math.cos(self.theta) * t # updates x positon
        self.y = self.y0 + self.v * math.sin(self.theta) * t - 4.9*(t**2.0) # updates y position
        canvas.create_rectangle((self.x,(mapping.get_height()-self.y))*2) # used for plotting the path of the ball
        canvas.coords(self.cannonBall, mapping.get_i(self.x) + 4, mapping.get_j(self.y) + 4,mapping.get_i(self.x) - 4, mapping.get_j(self.y) - 4)

    def get_x(self): # returns x position
        return self.x

    def get_y(self): # returns y position
        return self.y

    def get_velocity(self): # returns velocity
        return self.v

    def stopped(self): # changes the ball color to red when called
        canvas.itemconfig(self.cannonBall, fill="red")

parameters=input("Enter both theta(0,90) and strength (return for default 60 degree and 0.75): ") # asks for input parameters
if parameters == "": # check if there was anything inputted, if nothing set theta and strength
    theta = 60
    strength = 0.75
else: # split inputted parameters to theta and strength respectively
    theta, strength = parameters.split()
mapping=Mapping_for_Tkinter(0.0,1200.0,0.0,400.0,1200) # define mapping
cannon=cannon_ball(theta, strength) # defines variable for class cannon_ball
window=Tk() # establishes window for tkinter
canvas= Canvas(window, width=mapping.get_width(), height=mapping.get_height()) #establish canvas size
cannon.create_oval() # creates the ball used in this section
canvas.pack() # draw the canvas
t=0               # real time between event
t_total=0         # real total time
rebound=0           # rebound_total=0
while True:
    t=t+0.1 #real time between events- in second
    t_total=t_total+0.1 #real total time- in second
    cannon.update_xy(t)# Update ball position and return collision event
    window.update()   # update the graphic (redraw)
    if cannon.get_y()<=mapping.get_ymin()+4: # if cannon ball hits bottom
        cannon.bounce() # call method bounce from class cannon_ball
        rebound+=1 # increment the number of rebounds
        t=0 # reinitialize the local time
    time.sleep(0.02)  # wait 0.01 second (simulation time)
    if cannon.get_velocity()<0.01 or cannon.get_x()>1200:
        cannon.stopped() # call method stopped from class cannon_ball
        break # stop the simulation
print("Total number of rebounds is: "+ str(rebound)) # print rebounds
print("Total real time is: "+ str(t_total)+"s") # print total time
print("Distance traveled is: "+ str(cannon.get_x())+"m") # print distance traveled
window.mainloop() # wait until the window is closed