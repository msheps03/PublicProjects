%Maxwell Shepherd ECE 202 Fall 2020, MATLAB Exercise M6, October 13, 2020
%Determining the final velocities of three carts in a given system, this is
%done through energy and momentum conservation, when final velocities are g
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
global m
m = input("Value for mass of carts 1, 2, and 3: ");
v = input("Value for velocity of carts 1, 2, and 3: ");
if v(3) < v(2) && v(2) < v(1)
    firstCollision = input("Which collision is first(12 or 23): "); 
else
    firstCollision = 0;
end
p0 = sum(m.*v); % initial momentum
E0 = sum(1/2*m.*v.^2); % initial kinetic energy
count = 0;

%====Collisions============================================================
while v(3) < v(2) || v(2) < v(1)
    count = count + 1;
    fprintf("Collision #%1.0f",count)
    v = velocity(v,firstCollision)
    firstCollision = 0; 
    EnergyCheck = E0-sum(1/2*m.*v.^2); % should display 0
    MomentumCheck = p0-sum(m.*v); % should display 0
    if abs(EnergyCheck)>1e-10
        fprintf("Energy Check is %4.4f, should be 0\n",EnergyCheck)
    elseif abs(MomentumCheck)>1e-10 
        fprintf("Momentum Check is %4.4f, should be 0\n", MomentumCheck)
    end
end
fprintf("There are no more collisions, %1.0f total collisions\n",count)

%====Function==============================================================
function vn = velocity(v,c)
    global m
    m12 = m(1)+m(2); % Mass of carts 1 and 2 grams
    m23 = m(2)+m(3); % Mass of carts 2 and 3 grams

    if v(3) < v(2) && c ~= 12
        vn = [v(1) (2*m(3)*v(3) + v(2)*(m(2)-m(3)))/m23 ...
            (2*m(2)*v(2) + v(3)*(m(3)-m(2)))/m23];
    else 
        vn = [(2*m(2)*v(2) + v(1)*(m(1)-m(2)))/m12 ...
            (2*m(1)*v(1) + v(2)*(m(2)-m(1)))/m12 v(3)];
    end
end
