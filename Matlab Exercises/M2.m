%Maxwell Shepherd ECE 202 Fall 2020, MATLAB Exercise M2, August 28, 2020
%Determining the final velocity of a moving object with final velocity of
%cart 2 and mass of cart 1 as unknowns
%cart 1 is the blue cart and cart 2 is the green cart, for reference
%negative is left
clear
%====Givens================================================================

m2 = 150; % grams
v1i = 30; % cm/s
v1f = 0; % final velocity of cart 1 cm/s
v2i = -30; % cm/s, negative because left is negative

%====Solving for Unknowns==================================================

m1 = m2*(2*v2i - v1i - v1f)/(v1f-v1i) % grams
M = m1+m2; % grams
v2f = (2*m1*v1i + v2i*(m2-m1))/M % final velocity of cart 2 cm/s


%==== Energy Equations & Energy Check======================================

E1i = 1/2*m1*v1i^2; % equation for kinetic energy of cart 1 hebdo-Joules
E2i = 1/2*m2*v2i^2; % equation for kinetic energy of cart 2 hebdo-Joules
E1f = 1/2*m1*v1f^2; % final energy of cart 1 Joules
E2f = 1/2*m2*v2f^2; % final energy of cart 2 Joules
Ei = E1i+E2i; % initial energy hebdo-Joules
Ef = E1f+E2f; % final energy in hebdo-Joules
EnergyCheck = Ei-Ef % energy conservation check, should be 0

%====Momentum Check========================================================

p0 = m1*v1i + m2*v2i; % inital momenutum of system
pf = m1*v1f + m2*v2f; % final  momentum of system
MomentumCheck = p0-pf % momentum conservation check, should be 0

%====Velocity Check========================================================

v1f = (2*m2*v2i + v1i*(m1-m2))/M % velocity equation from m1, should be 0

if abs(v1f) < 0.0001
    disp("Design Criteria Met")
end

%====Citations=============================================================
%Momentum Conservation: “Momentum Conservation Principle.” The Physics Clas
%sroom, www.physicsclassroom.com/class/momentum/Lesson-2/Momentum-Conservat
%ion-Principle.
%Energy Conservation: “Conservation of Energy.” Conservation of Energy, 199
%9, physics.bu.edu/~duffy/py105/EnergyConservation.html.