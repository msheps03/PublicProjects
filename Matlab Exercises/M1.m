%Maxwell Shepherd ECE 202 Fall 2020, MATLAB Exercise M1, August 27, 2020
%Determining the final velocities of two carts given their initial mass and
%velocities
%cart 1 is the blue cart and cart 2 is the green cart, for reference
%negative is left
clear
%====Givens================================================================

m1 = 250; % grams
m2 = 150; % grams
M = m1+m2; % grams
v1i = 40; % cm/s
v2i = -30; % cm/s, negative because left is negative

%====Velocity Equations====================================================

v1f = (2*m2*v2i + v1i*(m1-m2))/M % final velocity of cart 1 cm/s
v2f = (2*m1*v1i + v2i*(m2-m1))/M % final velocity of cart 2 cm/s

%====Energy Check==========================================================

E1i = 1/2*m1*v1i^2; % equation for kinetic energy of cart 1 ergs
E2i = 1/2*m2*v2i^2; % equation for kinetic energy of cart 2 ergs
Ei = E1i+E2i; % initial energy ergs
E1f = 1/2*m1*v1f^2; % final energy of cart 1 ergs
E2f = 1/2*m2*v2f^2; % final energy of cart 2 ergs
Ef = E1f+E2f; % final energy of system in ergs
EnergyCheck = Ei-Ef % energy conservation check, should be 0

%====Momentum Check========================================================

p0 = m1*v1i + m2*v2i; % inital momenutum of system
pf = m1*v1f + m2*v2f; % final  momentum of system
MomentumCheck = p0-pf % momentum conservation check, should be 0

%====Citations=============================================================
%Momentum Conservation: “Momentum Conservation Principle.” The Physics Clas
%sroom, www.physicsclassroom.com/class/momentum/Lesson-2/Momentum-Conservat
%ion-Principle.
%Energy Conservation: “Conservation of Energy.” Conservation of Energy, 199
%9, physics.bu.edu/~duffy/py105/EnergyConservation.html.