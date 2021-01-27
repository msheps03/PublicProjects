%ECE 202 Fall 2020 Exercise M4 part A, Maxwell Shepherd, 9-9-2020
%Plotting a truncated power series

clear
t = linspace(0,6,401); % use 400 values of t from 0 to 6
ft = 1 + t/2 - (1/3)*t.^2; % seconds, bound from t = 0 to t = 6

plot(t,ft,'LineWidth',3)
ax = gca; ax.FontSize = 14;
title({'ECE 202 Exercise M4 Part A', 'Truncated Power Series'},'FontSize', 14)
xlabel('Time (s)', 'FontSize', 16)
ylabel('f(t)', 'FontSize', 16)
grid on