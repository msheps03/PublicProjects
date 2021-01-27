from Mapping_for_Tkinter import Mapping_for_Tkinter
from racket import racket
from ball import ball
from tkinter import*
import time
#all the stuff i need
window=Tk() # intializes window for tkinter
mapping=Mapping_for_Tkinter(-300.0,300.0,-300.0,300.0,600) # intializes mapping
canvas= Canvas(window, width=mapping.get_width(), height=mapping.get_height()) # intializes canvas
canvas.pack() # draws the canvas
velocity=200 # intialize velocity
angle=53 # intialize angle
#creating ball
ball1=ball(mapping,canvas,0,mapping.get_ymin()+14,velocity,angle) # bind class ball to ball1
ball1.create_oval() # create ball
#creating racket
myracket=racket(canvas,0,-295,mapping) # bind class racket to myracket
myracket.create_rectangle() # create racket
#binding mouse clicks
canvas.bind("<Button-1>", lambda e: myracket.shift_left())
canvas.bind("<Button-3>", lambda e: myracket.shift_right())
#simulation
t = 0  # real time between event
t_total = 0  # real total time
count = 0  # rebound_total=0
while True:
    t = t + 0.01  # real time between events- in second
    t_total = t_total + 0.01  # real total time- in second
    side = ball1.update_xy(t,"game1",velocity)  # Update ball position and return collision event
    window.update()  # update the graphic (redraw)
    if side != 0: # if not hitting a side
        count = count + 1  # increment the number of rebounds
        t = 0  # reinitialize the local time
    if side == 2: # if hitting top increase velocity by 25%
        velocity=velocity*1.25
    if side == 1: # if hitting the bottom
        if myracket.get_xracket()-30>ball1.get_xball() or ball1.get_xball()>myracket.get_xracket()+30: # without hitting paddle
            print("Game over! Total time: "+ str(t_total)) # prints total time lasted
            break # breaks loop
    time.sleep(0.01)  # wait 0.01 second (simulation time)