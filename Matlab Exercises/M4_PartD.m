%ECE 202 Fall 2020 Exercise M4 part A, Maxwell Shepherd, 9-9-2020
%Plotting Three Dampings for Parallel RLC

clear
tms = linspace(0,40,401); % use 400 values of t from 0 to 40 ms
t = tms/1000; % make t in s
v1t = 16*exp(-800*t) - 4*exp(-200*t) ; % ms
v2t = exp(-500*t).*(6 - 6000*t); %ms
v3t = exp(-120*t).*(12*cos(450*t) - 5*sin(450*t)); %ms

plot(t,v1t,'r',t,v2t,'g',t,v3t,'b','LineWidth', 3)
ax = gca; ax.FontSize = 14;
title({'ECE 202 Exercise M4 Part D','Three Dampings for Parallel RLC'},...
    'FontSize', 24)
xlabel('Time (ms)', 'FontSize', 18)
ylabel('Voltage (V)', 'FontSize', 18)
legend('overdamped','critically damped','underdamped','FontSize',20)
grid on