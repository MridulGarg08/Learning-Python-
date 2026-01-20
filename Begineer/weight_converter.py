# Weight Converter
weight=float(input("Enter your weight!"))
unit=input("Enter unit (L) bs or (K)g: ")
unit=unit.upper()
if(unit=='L'):
    con_weight=weight*0.45
else:
    con_weight=weight/0.45

print(con_weight)