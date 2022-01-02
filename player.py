import random
import question_bank

class Player:
    def __init__(self, name):
        self.name = name

    def greeting(self, name):
        return "Welcome {name}! Here is your first question...".format(name=self.name) + "\n"

    def answer_choice(self, correct_answer):
        print("What do you want to do?")
        print("Answer: 1")
        print("Use Lifeline: 2\n")
        option = input("Choose an option: \n")
        if option == "1":
            answer = input("What is the answer?: ")
            if answer not in ["A", "B", "C", "D"]:
                return "Please enter A, B, C or D"
            elif answer == correct_answer:
                return "CORRECT!"
                # Variable here to add to money total
            else:
                return "You haven't answered correctly, better luck next time!"

        if option == "2":
            input("Which lifeline would you like to use? \n== 50/50 == Call a Friend == Ask the Audience ==")
    