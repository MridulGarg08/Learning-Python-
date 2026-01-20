import random
secret_num=random.randrange(10,20,1)
print(secret_num)
i=1
is_won=False
while(i<=3):
    choice=int(input("Enter your choice!!!"))
    if(choice==secret_num):
        is_won=True
        break
    else:
        print("Try Again!!!")
    i+=1
if(is_won):
    print("Heya!!  You won!!!")
else:
    print("You lose!!! Better Luck next Time")
