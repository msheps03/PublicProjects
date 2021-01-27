from Mapping_for_Tkinter import Mapping_for_Tkinter
from racket import racket
from ball import ball
from tkinter import*
import time

window=Tk() # establishes window for tkinter
mapping=Mapping_for_Tkinter(-300.0,300.0,-300.0,300.0,600) # define mapping
canvas= Canvas(window, width=mapping.get_width(), height=mapping.get_height()) #establish canvas size
canvas.pack()  # draw the canvas
velocity=300 # initialize velocity
angle=45 # intialize angle
myturn=False # top paddle goes first
#creating ball
ball1=ball(mapping,canvas,0,mapping.get_ymin()+14,velocity,angle) # binds class ball to ball1
ball1.create_oval() # creates ball
#creating rackets
myracket=racket(canvas,0,-295,mapping) # binds bottom racket to myracket
yourracket=racket(canvas,0,290,mapping) # binds top racket to yourracket
myracket.create_rectangle() # creates bottom racket
yourracket.create_rectangle() # creates top racket

#simulation
t = 0  # real time between event
t_total = 0  # real total time
count = 0  # rebound_total=0
while True:
    t = t + 0.01  # real time between events- in second
    t_total = t_total + 0.01  # real total time- in second
    side = ball1.update_xy(t,"game2")  # Update ball position and return collision event
    window.update()  # update the graphic (redraw)
    if side != 0: # if ball hits a side
        count = count + 1  # increment the number of rebounds
        t = 0  # reinitialize the local time
    if side == 2: # if ball hit top
        myturn=True # bottom paddle's turn
        if yourracket.get_xracket()-30>ball1.get_xball() or ball1.get_xball()>yourracket.get_xracket()+30:
            loser="2" # intialize who lost
            print("Game Over for Racket "+ loser + "!") # print who lost
            break # break loop
    if side == 1: # if ball hit bottom
        myturn=False # top paddle's turn
        if myracket.get_xracket()-30>ball1.get_xball() or ball1.get_xball()>myracket.get_xracket()+30:
            loser="1" # initialize who lost
            print("Game Over for Racket "+ loser + "!") # print who lost
            break # break loop
    if myturn: # if bottom paddles turn
        canvas.bind("<Button-1>", lambda e: myracket.shift_left())
        canvas.bind("<Button-3>", lambda e: myracket.shift_right())
        myracket.activate() # turn bottom racket red
        yourracket.deactivate() # turn top racket black
    else: # if top paddles turn
        canvas.bind("<Button-1>", lambda e: yourracket.shift_left()) # move left with left click
        canvas.bind("<Button-3>", lambda e: yourracket.shift_right()) # move right with right click
        yourracket.activate() # turn top racket red
        myracket.deactivate() # turn bottom racket black
    time.sleep(0.01)  # wait 0.01 second (simulation time)