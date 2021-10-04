import random

class Thrower:
    """A code template for the actions in the game
    a throwers responsability is to hold all the code for
    the actions that the game needs to perform

    Attributes
        init:
        can_throw:
        get_points:
        throw_dice:
    """

    def __init__(self):
        #A)sets default values. B) C)default values.
        self.dice = []
        self.num_throws = 0
        
    
    def can_throw(self):
        #A)checks can it throw again? B) C)Boolean
        return (self.dice.count(1) > 0 or self.dice.count(5) > 0 or self.num_throws == 0)
    
    def get_points(self):
        #A)adds up points
        self.ones = self.dice.count(1) * 100
        self.fives = self.dice.count(5) * 50
        return self.ones + self.fives

    def throw_dice(self):
        #A)gets 5 random numbers B) C)list
        ran_1 = random.randint(1,6)
        ran_2 = random.randint(1,6)
        ran_3 = random.randint(1,6)
        ran_4 = random.randint(1,6)
        ran_5 = random.randint(1,6)
        self.dice = [ran_1, ran_2, ran_3, ran_4, ran_5]