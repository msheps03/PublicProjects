%ECE 202 Fall 2020 Exercise M4 part C, Maxwell Shepherd, 9-9-2020
%Plotting a Normalized Gaussian

clear
x = linspace(0,10,401); % use 400 values of x from 0 to 10
Px = 1/(2*sqrt(pi))*exp(-((x-5).^2)/4); % inverse meters

plot(x,Px,'--','LineWidth',3)
ax = gca; ax.FontSize = 14;
title({'ECE 202 Exercise M4 Part C', 'Normalized Gaussian plot'},...
'FontSize', 24)
xlabel('x (m)', 'FontSize', 18)
ylabel('Probability Density, m^-^1', 'FontSize', 18)
grid on