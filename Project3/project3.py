import matplotlib.pyplot as plt
import numpy as np
import sklearn.metrics as skm

data = open("walmart_data.txt","r") # open the text file as data
pop = [] # Initialize empty list for populations
profit = [] # Initialize empty list for profits
for line in data: # Analyze data by each line
    new = line.split(",")
    pop.append(float(new[0])) # Append population
    profit.append(float(new[1])) # Append profit

plt.scatter(pop,profit) # Scatter plot with population as x axis and profit as y axis
npPop = np.array(pop) # Create a numpy array of population
npProfit = np.array(profit) # Create a numpy array of profit
mb = np.polyfit(npPop, npProfit, 1) # Returns a list with slope and y intercept
m = mb[0] # Define slope
b = mb[1] # Define y intercept
plt.plot(npPop, m * npPop + b, 'r') # Plot the line of best fit using y intercept and slope, make the color red
plt.xlabel('Population (x10,000)')
plt.ylabel("Profit (x10,000)")
plt.show()

newPop = [7.8, 4.4, 4.7, 6.12, 8.55, 6.7, 9.8, 7.01] # List of new Populations
keys = ["A","B","C",'D','E','F','G','H'] # List of keys corresponding to new population
newProfit = {} # Create an empty dictonary
for i in range(len(newPop)):
    newProfit[keys[i]] = newPop[i]*m + b # For each dictionary key, append the new population

sortedProfits = sorted(newProfit.items(), key=lambda x:x[1], reverse=True) # Sort the dictionary by profits
sortedKeys = ""
for i in sortedProfits: # sortedKeys becomes list of greatest to least profit
    sortedKeys+=i[0] + " "
predictedProfit = [] # list of predicted profits for use in mae
for i in range(len(profit)):
    predictedProfit.append(m*pop[i] + b)

mae = skm.mean_absolute_error(profit,predictedProfit)
