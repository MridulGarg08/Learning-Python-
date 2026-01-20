customer=[
    {
    "name":"Mridul Garg",
    "age":23,
    "is_verified":True
    },
    {
    "name":"Prince Garg",
    "age":25,
    "is_verified":False
    }
]
customer2={
    "name":"Mridul Garg",
    "age":23,
    "is_verified":True
    }

#Both below methods can be used to access keys from the dictionary
# print(customer["name"]) # to access
# print(customer.get("name")) # to access
print(customer[0].get("name"))   

for obj in customer:  # Looping across the dictionary
    print(obj.get("name"))
    
#We can also update the attributes using assignment operator like below
customer2["name"]="Garg"
print(customer2.get("name"))
