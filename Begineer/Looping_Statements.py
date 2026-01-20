import random
#While Statements

i=1
while(i<=5):
    print(i)
    i+=1
    
i=1
while(i<=5):
    print("*" *i)
    i+=1
    
# Only difference in looping statements is that we use paranthesis in java looping statements

#For loop

for char in 'Python':
    print(char)

for item in ["Mridul","Shubhi","Pooja","Sandeep"]:
    print(item)

arr=[10,20,30,40,50]
for num in arr:
    print(num)

for i in range(10):
    print(i)

for i in range(5,10,2):
    print(i)

for x in range(4): 
    for y in range(3):
        print(f"x={x} and y={y}")

list=[5,2,5,2,2]
for item in list:
    print("*"*item)