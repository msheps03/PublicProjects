%Maxwell Shepherd ECE 202 Fall 2020, MATLAB Exercise M3, September 3, 2020
%Determining the final velocities of three carts in a given system, this is
%done through energy and momentum conservation
%cart 1 is the red cart, cart 2 is the blue cart, and cart 3 is the green 
%cart
%A,B,C,D, and E refer to first, second, third, fourth and fifth collisions 
%respectively
%negative is left

%====Citations=============================================================
%Momentum Conservation: “Momentum Conservation Principle.” The Physics 
%Classroom, www.physicsclassroom.com/class/momentum/Lesson-2/Momentum-Conse
%rvation-Principle.
%Energy Conservation: “Conservation of Energy.” Conservation of Energy
%, 1999, physics.bu.edu/~duffy/py105/EnergyConservation.html.

clear
%====Initial Values========================================================

m = [240 120 360]; % grams
vi = [30 15 -45]; % cm/s
m23 = m(2)+m(3); % grams
m12 = m(1)+m(2); % grams
p0 = sum(m.*vi); % initial momentum
E0 = sum(1/2*m.*vi.^2); % initial kinetic energy

%====Collision A===========================================================

vA = [vi(1) (2*m(3)*vi(3) + vi(2)*(m(2)-m(3)))/m23 ...
    (2*m(2)*vi(2) + vi(3)*(m(3)-m(2)))/m23]
EnergyCheckA = E0-sum(1/2*m.*vA.^2) % should display 0
MomentumCheckA = p0-sum(m.*vA) % should display 0

%====Collision B===========================================================

vB = [(2*m(2)*vA(2) + vA(1)*(m(1)-m(2)))/m12 ...
    (2*m(1)*vA(1) + vA(2)*(m(2)-m(1)))/m12 vA(3)]
EnergyCheckB = E0-sum(1/2*m.*vB.^2)
MomentumCheckB = p0-sum(m.*vB)

%====Collision C===========================================================

if vB(3) < vB(2) || vB(2) < vB(1)
    disp("There is another Collision")
else
    disp("There are no more collisions")
    Collisions = 2
end
vC = [vB(1) (2*m(3)*vB(3) + vB(2)*(m(2)-m(3)))/m23 ...
        (2*m(2)*vB(2) + vB(3)*(m(3)-m(2)))/m23]
    EnergyCheckC = E0-sum(1/2*m.*vC.^2) % should display 0
    MomentumCheckC = p0-sum(m.*vC) % should display 0

%====Collision D===========================================================

if vC(3) < vC(2) || vC(2) < vC(1)
    disp("There is another Collision")
else
    disp("There are no more collisions")
    Collisions = 3
end
vD = [(2*m(2)*vC(2) + vC(1)*(m(1)-m(2)))/m12 ...
        (2*m(1)*vC(1) + vC(2)*(m(2)-m(1)))/m12 vC(3)]
    EnergyCheckD = E0-sum(1/2*m.*vD.^2) % should display 0
    MomentumCheckD = p0-sum(m.*vD) % should display 0

%====Collision E===========================================================

if vD(3) < vD(2) || vD(2) < vD(1)
    disp("There is another Collision")
else
    disp("There are no more collisions")
    Collisions = 4
end

