%Maxwell Shepherd ECE 202 Fall 2020, MATLAB Exercise M5, September 9, 2020
%Finding two sinusoids that when added together will equal a given function
%identity: K*cos(x)*cos(y) = (K/2)*[cos(x-y) + cos(x+y)]

%====Citation==============================================================

%Stapel, Elizabeth. “Trigonometric Identities.” Purplemath, www.purple
%math.com/modules/idents.htm. 

clear
clf

tms = linspace(0,200,401); % initialize a time array from 0 to 200 ms
t = tms/1000; % convert milliseconds to seconds
x = 60*t-1.8; 
y = 100*t+1.2;
K = 12;
ft = K*cos(x).*cos(y); % initial function
f1t = K/2*cos(x-y); % function 1
f2t = K/2*cos(x+y); % function 2
FunctionCheck = ft-f1t-f2t;

plot(tms,ft,tms,f1t,tms,f2t,tms,FunctionCheck,'LineWidth', 3)
ax = gca; ax.FontSize = 14;
title({'ECE 202 Exercise M5', ...
    'Solving K*cos(x)*cos(y) for (K/2)*[cos(x-y) + cos(x+y)]'},...
    'FontSize', 24)
xlabel('Time (ms)', 'FontSize', 18)
ylabel('f(t)', 'FontSize', 18)
legend('f = Product','f_1=1^s^t Term','f_2=2^n^d Term',...
'Check=f - (f_1+f_2), should be 0','FontSize',14)
ylim([-20,20])
grid on

EqualityCheck = sum(abs(FunctionCheck)) % should return a value close to 0

%The absolute value function is utilized in order to prevent a problem with
%adding signs. If there are both negative and positive values when summed
%together would still be zero even though the functions are incorrect