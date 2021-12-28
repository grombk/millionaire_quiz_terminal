import random
import question_bank

class Player:
    def __init__(self, name):
        self.name = name

    def greeting(self, name):
        return "Welcome {name}! Here is your first question...".format(name=self.name)
    