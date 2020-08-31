#Project 3 Question 1
print("This program will determine the product of two positive integers")
print("Enter two zeros to exit the program")
multiplier=int(input("Please enter the multiplier: "))
multiplicand=int(input("Please enter the multiplicand: "))
    
print("Multiplier: ",multiplier)
print("Multiplicand: ",multiplicand)
print("Calculating product: ")
while(multiplicand!=0 and multiplier!=0):#program will keep running until the user enters two zeros
    if(multiplier<0 or multiplicand<0): #if its negative
        print("Values must not be negative")
        multiplier=int(input("Please enter the multiplier: ")) #continues program
        multiplicand=int(input("Please enter the multiplicand: "))
    if(multiplicand%2!=0):#if its odd
        answer=0 #so everything added will be the answer
        print(multiplier, multiplicand)
        answer=answer+multiplier #add multiplier to answer
    else: #if its even,
        answer=0 #you don't add the multiplier to the answer
        multiplier=multiplier*2 #calculating
        multiplicand=multiplicand//2
        if(multiplicand%2!=0):#if after all calculations, the multiplicand is odd
            print(multiplier, multiplicand)
            answer=answer+multiplier
            
    while(multiplicand>1): #if multiplicand is <0 then its time to print the answer
        multiplier=multiplier*2
        multiplicand=multiplicand//2
        if(multiplicand%2!=0):
            print(multiplier, multiplicand)
            answer=answer+multiplier
        else:
            multiplier=multiplier*2
            multiplicand=multiplicand//2
            if(multiplicand%2!=0):
                print(multiplier,multiplicand)
                answer=answer+multiplier
        
            
    print("Product:",answer) #prints after multiplicand is 1
    multiplier=int(input("Please enter the multiplier: ")) #continues the program
    multiplicand=int(input("Please enter the multiplicand: "))
print("Have a good day") #prints when user enters 0
