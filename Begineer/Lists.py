import math
list=["Mridul","Shubhi","Pooja","Sandeep"]
print(list[-1])
print(list[2:]) # Will not modify the original list
print(list[2:3])
list[0]="Garg" #Will modify the list as array in java
print(list)

list2=[50,-math.inf,2,8,79]
maxi=0   # can be initialized to math.inf 
mini=-1  # can be initialized to -math.inf 
for item in list2:
    if(item>maxi):
        maxi=item
    if(item<mini):
        mini=item
print(maxi)
print(mini)

#2d Lists
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix)

for item in matrix:
    for i in item:
        print(i,end=" ") # used to print space after element
    print()
        
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j])

matrix[0][1]=100

for item in matrix:
    for i in item:
        print(i,end=" ") # used to print space after element
    print()
    
# marks=[80,90,70,65,85]
# marks.

#   COMPLETE SUMMARY TABLE
# Operation	               Java ArrayList	   Python List
# Add end	                  add()	             append()
# Add index	                add(i, x)	         insert(i, x)
# Add multiple	             addAll()	         extend()
# Remove index	             remove(i)	         pop(i)
# Remove value	             remove(obj)	     remove(x)
# Access	                  get(i)	         lst[i]
# Modify	                  set(i,x)	         lst[i]=x
# Size	                      size()	         len()
# Sort	                 Collections.sort()	     sort()
# Reverse	             Collections.reverse()   reverse()
# Copy	                    Constructor	         copy()

#WAP to remove duplicates in alist

arr=[10,20,40,10,20,60,80,60]
arr.sort()
unique=[arr[0]]
print(arr)

for i in range(1,len(arr)):
    if(arr[i]!=arr[i-1]):
        unique.append(arr[i])  # If you modify while looping then it will create problems
print(unique)

unique2=[]
for i in arr:
    if(i not in unique2):
        unique2.append(i)  
print(unique2)

print(type(unique2))

maximum=max(unique2) #to find max same min() for minimum
print(maximum)