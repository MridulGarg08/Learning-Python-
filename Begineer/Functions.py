def greet():    #With no parameters
    print("Hello There!!")
    return "Mridul"
    
# print(greet())

def greetme(Name):     # With single parameter
    print(f"Hello {Name}")
    return Name

def greettwo(Name1,Name2):   # With two parameters
    print(f"Hello {Name1} with {Name2}")
    return "Both greeted"


# print(greetme("Mridul Garg"))
# print(greettwo("Prince", "Prinshu"))

#From this we get to know that everything is same as java jusr small syntactical differences

# print(greettwo(Name2="Prince", Name1="Prinshu")) 

# If we want to flipp the arguments or want to assign inorderly then we can use keyword arguments but we cant flip and give single keyword to one

# print(greettwo("Prince", Name1="Prinshu")) #We flipped here but as Prince is assigned to Name1 and Prinshu is also assigned to Name1 This results in an error as Name1 is getting assigned twice 


def calcost(cost, discount):
    finalcost=cost-((discount/100)*cost)
    return finalcost

# print(calcost(1000,10))

def calsquare(num):
    return num*num

print(calsquare(int(input("Enter your number!!!"))))

# If we dont have return statement and we try to print then we will get None as output bacause by default python returns None from a function
    
    