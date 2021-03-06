import random

# You have a Dice class which has 6 dice
# You can roll all of them with roll()
# Check the current rolled numbers with get_current()
# You can reroll with reroll()
# Your task is to get where all dice is a 6

class Dice(object):

    def __init__(self):
        self.dice = [0, 0, 0, 0, 0, 0]

    def roll(self):
        for i in range(len(self.dice)):
            self.dice[i] = random.randint(1,6)
        return self.dice

    def get_current(self, index=None):
        if index != None:
            return self.dice[index]
        else:
            return self.dice

    def reroll(self, index=None):
        if index != None:
            self.dice[index] = random.randint(1,6)
        else:
            self.roll()

dice = Dice()

for i in range(len(dice.dice)):
    while dice.get_current(i) != 6:
        dice.reroll(i)

print(dice.get_current())
