%Maxwell Shepherd ECE 202 Fall 2020, Matlab Exercise M7, October 13, 2020
%Plotting values for current, voltage and power in a given circuit
%containing a resistor, power source, and inductor

clear
clf
%====Givens================================================================
V0 = 10; %Volts across source
L = 50; %MilliHenry
R = 2; %Ohms
T = L/R; % Time constant, Tau in ms
tmin = 0; % Left bound on graph
tmax = 10*T; % Right bound on graph, in ms
N = 401; % Intervals
t = linspace(tmin,tmax,N); % Time in ms
dt = (tmax-tmin)/N; % change in time in ms
e = exp(-t/T);

%====Calculations==========================================================
iFinal = V0/R; % t = inf, therefore i = V0/R, iFinal is in Amps
it = iFinal*(1 - e); % Current in Amps
V = V0*e; % Voltage in volts, across inductor
pt = V.*it; % Power in Watts
wF = 0.5*L*iFinal^2 % Final Energy stored in the Inductor, Ergs
wAbs = trapz(t,pt) % Energy absorbed by inductor in, Ergs
nrgDif = wF - wAbs % Ergs
EnergyPctError = 100*nrgDif/wAbs


subplot(3,1,1)
plot(t,it,'r','linewidth',2)
ylabel('Current (Amps)', 'FontSize', 12)
text(170,1.2,sprintf('$$ i(t)=%g\\cdot(1-e^{-t/%g}) $$',iFinal,T),...
    'FontSize',15,'Interpreter','latex')
ylim([0,6])
yticks([0 2 4 6])
grid on

subplot(3,1,2)
plot(t,V,'b','linewidth',2)
text(180,8,sprintf('$$ v(t)=%g\\cdot e^{-t/%g} $$',V0,T),...
    'FontSize',15,'Interpreter','latex')
ylabel('Voltage (Volts)','FontSize', 12)
ylim([0,10])
grid on

subplot(3,1,3)
plot(t,pt,'g','linewidth',2)
ylabel('Power Absorbed (W)','FontSize', 12)
xlabel('Time (ms)')
text(190,13,'$$ p(t)=v(t) \cdot i(t) $$','FontSize',15,...
    'Interpreter','latex')
ylim([0,15])
grid on

sgtitle({'ECE 202 Fall 2020 Exercise M7',...
    'Current, voltage, and power absorbed for a charging inductor',...
    sprintf('$$ (V_o = %g V,R = %g \\Omega, L = %g mH)$$',V0,R,L)},...
    'Interpreter','latex')
