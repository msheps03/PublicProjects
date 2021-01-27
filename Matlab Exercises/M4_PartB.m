%ECE 202 Fall 2020 Exercise M4 part B, Maxwell Shepherd, 9-9-2020
%Plotting a shifted sinusoid

clear
x = linspace(-5,5,401); % use 400 values of x from -5 to 5
gx = 4*cos(3*(x-2)); % seconds, bound from t = 0 to t = 6

plot(x,gx,'r','LineWidth',3)
ax = gca; ax.FontSize = 14;
title({'ECE 202 Exercise M4 Part B', 'Shifted Sinusoid'},'FontSize', 14)
xlabel('x (m)', 'FontSize', 16)
ylabel('g(x)', 'FontSize', 16)
ylim([-6 6])
grid on