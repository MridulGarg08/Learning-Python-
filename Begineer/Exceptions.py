# try:
#     age=int(input("Enter Age: "))
#     print(age)
# except ValueError:
#     print("Error Occurred!!!")
# except:
#     print("Ertrior Occurred!!!")

try:
    age=int(input("Enter Age: "))
    income=20000
    risk=income/age
    print(age)
except ZeroDivisionError:
    print("Age cannot be Zero!!!")
except ValueError:
    print("Error Occurred!!!")