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
# message=f"{first} [{last}] is a great coder!!!"  # Formatted string
print(message)