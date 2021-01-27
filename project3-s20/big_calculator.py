'''------------------------------------------------------
                 Import Modules 
---------------------------------------------------------'''

from BigNumber import BigNumber

        
'''------------------------------------------------------
                Main program starts here 
---------------------------------------------------------'''

print("\nWelcome to BigNumber Calculator")
print("================================")

# closed loop, keep executing until user select 0
while True:
    command=input("\nChoose Operation (none,==,+,-,scale,*) or q for quit: ")

    if command=="q": #exit program
        print("Goodbye!")
        break

    # input error handling
    if not(command in ["none","==","+","-","scale","*"]):
           continue
    
    # read and convert first input string to a BigNumber
    big1=BigNumber(input("Enter first number: "))
    print(big1) # display
    
    if not(command in ["none","scale"]):
        # read and convert second input string to a BigNumber
        big2=BigNumber(input("Enter second number: "))
        print(big2) # display

    if command=="scale": # scale the big number and return a new big number
        factor=int(input("Enter the scaling factor: "))
        big3=big1.scale(factor)
        print("Result: "+str(big3))
     
    elif command=="==": # compare the two big numbers
        c=big1.compare(big2)
        print("first number %s second number"%c)

    elif command=="+": # perform big number addition and display
        big3=big1.add(big2)
        print("Result: "+str(big3))
        
    elif command=="-": # perform big number subtraction and display
        big3=big1.subtract(big2)
        print("Result: "+str(big3))
        
    elif command=="*": # perform big number multiplication and display
        big3=big1.multiply(big2)
        print("Result: "+str(big3))
