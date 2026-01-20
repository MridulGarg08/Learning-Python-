class Point_Table:
    def __init__(self,y,z):
        self.y=y
        self.z=z
    def __init__(self):  # This constructor will override the first as python doesnot support constructor overloading
        self.y=50
        self.z=500
    
    def move(self):
        print("Move")
    
    def draw(self):
        print("Draw")
        
 # Same as java but as no new keyword and there is no datatype so there is no new keyword and no datatype before object reference
point1=Point_Table()
point1.draw()

point1.x=10
print(point1.x) # We can create instance variables here also and we dont need to define it prior in class 
print(point1.y)
point1.y=150
print(point1.y)

point2=Point_Table()
point2.x=1
print(point2.x)  

point3=Point_Table(800,900)
print(point3.y)
print(point3.z)