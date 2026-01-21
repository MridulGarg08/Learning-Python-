import random
class diceroll:
    def roll(self):
        first=random.randint(1,6)
        second=random.randint(1,6)
        return first,second

dice=diceroll()
list=dice.roll()
print(list)
# print(dice.roll()) #can also do this