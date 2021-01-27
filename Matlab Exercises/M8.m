% Maxwell Shepherd
% 11/02/2020
% ECE 202 Fall 2020
% Exercise M8: Evaluating the ratio of two polynomials
% Utilizing partial fraction decomposition to allow for an analytical
% integral to be taken without changing the form of the function

clear
%====Matrix Operations, set up from hand calculation=======================
M = [1 1 1;-5 -4 -3;6 3 2];

b = [4; 5; 6];
C = M^(-1) * b

%====Evaluating R(x)=======================================================
N = input("N: "); % Number of points
x = linspace(-4,4,N); % Set up array of x values with N number of points

D1 = x-1; D2 = x-2; D3 = x-3;
R = C(1)./D1 + C(2)./D2 + C(3)./D3;
Nx = b(1).*x.^2 + b(2).*x + b(3)*1;
Dx = D1.*D2.*D3;
Rx = Nx./Dx;

Check = sum(Rx)-sum(R)

% N = 5: x = [-4 -2 0 2 4] R = [-0.24 -0.2 -1 -inf 15], check = NaN
% N = 6: x = [-4 -2.4 -0.8 0.8 2.4 4] R = [-0.24 -0.21 -0.4 -23.8 -122 15]
% check = -8.5265e-14
% When there are 5 intervals, the array R contains a value of -inf
% When there are 6 intervals, the array R does not contain a value of -inf
% Whenever there is a value of -inf in R the check is inappropriate. This
% is because -inf - -inf or inf - inf, is not a real number. This failure
% will repeat for N = 5,9,13... etc
% The -inf value comes from dividing by 0, which means this occurs when 
% x = 1, 2, or 3