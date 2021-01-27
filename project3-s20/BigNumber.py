class BigNumber:
    
    def __init__(self,string_big=None):
        """ constructor for class BigNumber """
        #initialize list
        self.list_big = [] # intializes list
        list_inefficient=[0,1,2,3,4,5,6,7,8,9] # created list to check if values inputted are integers
        self.list_check=[string_big[i:i+1] for i in range(0,len(string_big), 1)]# appends input to a list "list_check"
        for value in self.list_check: # for loop that removes all non integer values and appends the integers to the list list_big
            if value != "0":
                for number in list_inefficient:
                    if value == str(number) :
                        self.list_big.append(value)

    def __str__(self):
        """ tostring method for class BigNumber """
        count = 0 # sets variable count to 0
        number="" # establishes variable number as a string
        for i in self.list_big: # count loop returns the number of digits in the input
            count+=1
        remainder=count%3 # gives remainder, for use to put x number of digits before first comma
        if remainder ==0: # condition to prevent erroneous comma being placed before number
            remainder=3
        for placeValue in self.list_big: # for loop with embedded conditional statement that appends the digits in the number to variable number, adds commas where necessary
            if remainder >0:
                number+=placeValue
                remainder-=1
            else:
                number+=","
                remainder=2
                number+=placeValue
        return number

    def compare(self,big2): # function to compare the values of two big numbers
        if len(self.list_big)>len(big2.list_big): # if big 1 is long therefore the value is greater, this conditional statement compares lengths to determine longer value
            return ">"
        elif len(self.list_big)<len(big2.list_big): # this conditional statement compares lengths to determine longer value
            return "<"
        elif len(self.list_big)==len(big2.list_big): # this conditional statement runs if both numbers are the same length
            for i in range(len(self.list_big)): # runs for each place value of the number
                if self.list_big[i] > big2.list_big[i]: # compares digit by digit if a digit is greater in big 1 or in big 2, the corresponding number is bigger
                    return ">"
                elif self.list_big[i] < big2.list_big[i]:
                    return "<"
            return "=="
    
    def add(self,big2): # function to add two big numbers
        if self.list_big > big2.list_big: # establishes which list is bigger
            biggerList=self.list_big
        else:
            biggerList=big2.list_big
        big3="" # creates a variable "big3" that will be the added number
        if len(self.list_big) == len(big2.list_big): # if both numbers are the same length will add each value in the lists together
            for i in range(len(biggerList)):
                big3+=str(int(self.list_big[i])+int(big2.list_big[i]))
            return big3
        elif len(self.list_big)>len(big2.list_big): # if big number 1 is greater than big number 2, adds 0s to the left of big number 2 until it is the same length as big number 1 then adds each place value
            newList=[]
            count=abs(len(self.list_big)-len(big2.list_big))# how many 0s need to be added to the smaller number
            while count != 0: # while loop to add zeros to left of integer
                newList.append(0) 
                count-=1
            for originalValue in big2.list_big:
                newList.append(originalValue)
            for i in range(len(biggerList)):
                big3+=str(int(self.list_big[i])+int(newList[i]))
            return big3
        else: # if big number 2 is greater than big number 1, adds 0s to the left of big number 1 until it is the same length as big number 2 then adds each place value
            newList=[]
            count = abs(len(self.list_big) - len(big2.list_big)) # how many 0s need to be added to the smaller number
            while count != 0: # while loop to add zeros to left of integer
                newList.append(0)
                count -= 1
            for originalValue in self.list_big:
                newList.append(originalValue)
            for i in range(len(biggerList)):
                big3 += str(int(big2.list_big[i]) + int(newList[i]))
            return big3
    
    def subtract(self,big2):
        """ subtract two big positive numbers self and big2 and
        return a big number"""

        return BigNumber("0")

     
    def scale(self,factor):
        """ multiply the big number by a factor, and
        return a big number--does not work in place"""
        return BigNumber("0")

    
    def multiply(self,big2):
        """ multiply 2 big positive numbers self and big2 and 
        return a big number-
        use successive additions with method 'add' and kernel method 'scale'"""        
        return BigNumber("0")
