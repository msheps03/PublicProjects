from Mapping_for_Tkinter import Mapping_for_Tkinter
from tkinter import *
import math
import time
import random

class ball:
    def __init__(self, mapping, canvas, x0, y0, velocity, angle, myball=None):  # constructor for class ball
        self.mapping = mapping
        self.canvas = canvas
        self.x0 = x0
        self.y0 = y0
        self.velocity=velocity
        self.angle=(angle*(math.pi/180)) # intializes angle as radians
        self.myball=myball
        self.x=x0
        self.y=y0

    def create_oval(self): # create the ball
        self.myball=self.canvas.create_oval(self.mapping.get_i(self.x)+4,self.mapping.get_j(self.y)+4,self.mapping.get_i(self.x)-4,self.mapping.get_j(self.y)-4,fill="blue")

    def update_xy(self,t,game=None,deltaV=0,gameFix1=0,gameFix2=0): # update x and  y position when called
        if game=="game1": # conditional statement to allow for collaboration with game1.py and game2.py
            gameFix1=10 # sets game fix to 10
            velocity=deltaV # velocity equals deltaV
        elif game=="game2":
            gameFix2=10 # sets gamefix 2 to 10
            velocity=self.velocity # sets velocity to self.velocity
        else:
            velocity=self.velocity # sets velocity to self.velocity
        self.x=self.x0+velocity*math.cos(self.angle)*t # updates x positon
        self.y=self.y0+velocity*math.sin(self.angle)*t # updates y positon
        self.canvas.coords(self.myball,self.mapping.get_i(self.x) + 4, self.mapping.get_j(self.y) + 4, self.mapping.get_i(self.x) - 4, self.mapping.get_j(self.y) - 4) # moves ball based upon new x and y
        if self.x<=self.mapping.get_xmin()+4: # if ball hits left side
            self.angle=math.pi-self.angle # invert angle
            self.x0=self.x # reset x0
            self.y0=self.y # reset y0
            return int(3) # returned value is used to determine which side is hit

        elif self.x>=self.mapping.get_xmax()-4: # if ball hits right side
            self.angle=math.pi-self.angle # invert angle
            self.x0 = self.x # reset x0
            self.y0 = self.y # reset y0
            return int(4) # returned value is used to determine which side is hit

        elif self.y<= self.mapping.get_ymin()+4+gameFix1+gameFix2:# if ball hits bottom
            if game=="game2": # if it is game 2
                self.angle = (random.randint(10, 170)) * math.pi / 180 # convert random angle to radians
            else:
                self.angle = -self.angle # invert angle
            self.x0 = self.x # reset x0
            self.y0 = self.y # reset y0
            return int(1) # returned value is used to determine which side is hit

        elif self.y>= self.mapping.get_ymax()-4-gameFix2: # if ball hits top
            if game=="game1" or game=="game2": # if a game is being played
                self.angle=(random.randint(-170,-10))*math.pi/180 # set random angle to radians
            else:
                self.angle=-self.angle # invert angle
            self.x0 = self.x # reset x0
            self.y0 = self.y # reset y0
            return int(2) # returned value is used to determine which side is hit

        else:
            return int(0) # returned value is used to determine which side is hit

    def get_xball(self):
        return self.x
    def get_yball(self):
        return self.y

def main():
        ####### to complete
        variables=input("Enter velocity and theta (return for default: 500 pixel/s and 30 degree): ")
        if variables=="":
            v=500
            theta=30
        else:
            v,theta=variables.split()
        v=int(v)
        theta=int(theta)
        window=Tk()
        mapping = Mapping_for_Tkinter(-300.0, 300.0, -300.0, 300.0, 600.0)
        canvas= Canvas(window, width=mapping.get_width(), height=mapping.get_height())
        canvas.pack()

        ####### code provided below
        ball1=ball(mapping,canvas,0,0,v,theta)
        ball1.create_oval()
        ############################################
        ####### start simulation
        ############################################
        t=0               # real time between event
        t_total=0         # real total time
        count=0           # rebound_total=0
        while True:
            t=t+0.01 #real time between events- in second
            t_total=t_total+0.01 #real total time- in second
            side=ball1.update_xy(t)# Update ball position and return collision event
            window.update()   # update the graphic (redraw)
            if side!=0:
                count=count+1 # increment the number of rebounds
                t=0 # reinitialize the local time
            time.sleep(0.01)  # wait 0.01 second (simulation time)
            if count==10: break # stop the simulation
            
        print("Total time: %ss"%t_total)
        window.mainloop() # wait until the window is closed

if __name__=="__main__":
    main()