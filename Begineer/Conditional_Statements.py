age=input("Enter your age!")
age=int(age)
if(age>25):
    print("Adult")
# elif(20<age<=25):
#     print("Teen")
elif(20<age and age<=25):   #Logical Operator and in python and && in java
    print("Teen")
else:
    print("Not Considered")
    
# price=100000
# has_good_credit=True

# if(has_good_credit):
#     down_payment=0.1*price
# else:
#     down_payment=0.2*price

# print(down_payment)

