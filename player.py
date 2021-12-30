import random
import question_bank

class Player:
    def __init__(self, name):
        self.name = name

    def greeting(self, name):
        return "Welcome {name}! Here is your first question...".format(name=self.name) + "\n"

    def answer_choice(self):
        print("What do you want to do?")
        print("Answer: 1")
        print("Use Lifeline: 2")
        option = input("Choose an option: ")
        if option == "1":
            answer = input("What is the answer?: ")
            # correct_answer = question_bank.QuestionBank.correct_answers[]
            if answer not in ["A", "B", "C", "D"]:
                print("Please enter A, B, C or D")
            

        if option == "2":
            input("Which lifeline would you like to use? \n== 50/50 == Call a Friend == Ask the Audience ==")
    