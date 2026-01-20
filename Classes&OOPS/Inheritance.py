class Mammal:
    def walk(self):
        print("Walk!!")
    
class Dog(Mammal):
    def bark(self):
        print("Bark!!")
        
class Cat(Mammal):
    def meow(self):
        print("Meow!!")

dog=Dog()
dog.walk()
dog.bark()

cat=Cat()
cat.walk()
cat.meow()