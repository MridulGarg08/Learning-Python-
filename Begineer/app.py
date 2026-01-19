import math
print("Hello World!!!")

print('*'*10)  #This will draw 10 asterisk but in java we dont have such thing

#Variables

price=10 # we dont need to define the data type of variable "Integers"
print(price)
price=50
print(price)
rating=4.9 # Floating type
is_published=False  # Bollean type : In java its "false" but in python its capital 'F'
print(is_published)
# name=input("What your name!!!\n")
# print("Hi!!"+name)  # In java we also use '+' operator to join strings 

# name=input("Whats your name??")
# color=input("What ypou fav color??")
# print(name+"'s " + "favourite color is " +color)
# print(f"{name}'s favourite color is {color}")


# Type Conversion
# num=input("Enter a number?")
# final_num=10-int(num)  #If we dont do this then output variable will be a string, 
# #Hence we are converting it to a integer data type to perform the operation
# print(final_num)

# num2=input("Enter your number2??")
# print(type(num2))
# num2=int(input("Enter your number2??"))
# print(10-num2)
# print(type(num2))

#Pounds to kgs

# wgtinpds=int(input("Enter weight in Pounds!"))
# wgtinkgs=wgtinpds*0.45
# print(wgtinkgs)

# Strings in Python

str="Python for beginners!!!"
print(str[0])
print(str[-1])
# Unlike in java, we use array like accessing in strings in python as there is no such charAt(0) thing in python

print(str[0:3]) #from 0 to 3rd not including 3rd
print(str[1:]) #from 1st to last not 0
print(str[:5]) #from 0 to 5th not including 
print(str[:])  #full string from start to end
another=str[:] #copying
print(another)
print(str[1:-1]) #this will minus 1 from the last and consider it as last index (-1)
print(str[-1]) # This will rerturn as last index if -2 second last then
# This works like what substring does in Java

first="John"
last="Smith"
message=first+" ["+last+"] is a great coder!!"
# message=f"{first} [{last}] is a great coder!!!"  # Formatted string used for dynamically inserting values to your string
print(message)

#String length

string="Python"
print(len(string))  #In java we use string.length()  in python we just use len()

print(string.upper()) # In java we use .toUpperCase()
print(string.lower()) # In java we use .toLowerCase()

print(string.find('Y'))  # used to find the inde of particular charactrer in a string.cases are sensitive for Y -1 for y 1 
print(string.find('tho'))  # In java, .indexOf() is used, works for substring as well

print(string.replace('P','JOY')) # Used to replace the character with some other character or sibstring with other substring same as in java

print("Yth" in string) # used to find if that particular character or string is there in the 'string' , this si also case sensitive

#String functions 

# len() 
# upper()  
# .lower()
# .find()
# .replace()
# '...' in string

#Arithmetic Operations

print(10/3) #same as in java but results in Integer in java but in floating type in python
print(10%3) #same as in java
print(10*3) #same as in java
print("hello "*3) #for strings multiply for occurences
print(10-3) #same as in java
print(10+3) #same as in java
print(10**3)  #for power
x=20
print(x)
x+=40  # Works as in java
print(x)

# Operator Precedence
y=50+9*5
print(y)
#Order
#Paranthesis --> Exponentiation --> multiplication/division/modulus --> Addition/Substraction
#If have same precedence then it will be evaluated from left to right

#Rounding Off Operations
x=2.9
print(round(x))

print(round(2.3))   # 2
print(round(2.7))   # 3
print(round(2.5))   # 2 
print(round(3.5))   # 4

# Python works similar to java until unless there is .5 in a number #In python if thre is .5 then it is always rounded up to nearest even integer but in java its always up to next in case of .5

#Absolute 
print(abs(-2.9)) #Always returns a positive number

#Mathematical Functions
print(math.ceil(2.9))
print(math.floor(2.9))

#Logical Operators

# and-> both conditions should be true -> && in java
# or-> atleast one should be true-> || in java
# not-> flipped value of True means should be false-> ! in java

#Comparison Operators

# > Greater than
# < Less than
# >= Greater than or Equal to
# <= Less than or Equal to

print("Entr Your name")
name=input()

len=len(name)
if(len<3):
    print("Name must be atleast 3 characters long!!!")
elif(len>50):
    print("Name can be a maximum of 50 characters!!!")  
else:
    print("Name looks good!!!")


 




