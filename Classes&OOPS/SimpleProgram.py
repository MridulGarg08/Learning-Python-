class Person:
    def __init__(self,name):
        self.name=name
    # def __init__(self):
    #     self.name="Shubhi"
    def talk(self):
        print(f"Hi! I am {self.name}")
        
person=Person("Mridul")
print(person.name)
person.talk()

