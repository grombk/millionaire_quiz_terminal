import random
import question_bank
import lifeline

class Player:
    cash_prize = 0
    questions_asked = 0

    def __init__(self, name):
        self.name = name

    def greeting(self, name):
        return "Welcome {name}! Here is your first question...\n".format(name=name)

    def answer_choice(self, question, correct_answer, name):
        print("What do you want to do?")
        print("1: Answer")
        print("2: Use Lifeline")
        print("3: Take the Money")
        option = input("Choose an option: \n")
        if option == "1":
            self.questions_asked += 1
            answer = input("What is the answer?: ")
            if answer not in ["A", "B", "C", "D"]:
                return "Please enter A, B, C or D"
            elif answer == correct_answer:
                if self.questions_asked == 1:
                    self.cash_prize = 1000
                    return "CORRECT! You are on £1,000"
                elif self.cash_prize < 1000000:
                    self.cash_prize *= 2
                    return "CORRECT! You are on £{:,}".format(self.cash_prize)
                elif self.cash_prize == 1024000:
                    return "CORRECT! Congratulations, you have won the top prize of £1,000,000!!!"        
            else:
                return "You haven't answered correctly, better luck next time!"

        
        if option == "2":
            print("Which lifeline would you like to use?")
            print("1: 50/50")
            print("2: Ask the Audience")
            print("3: Call a Friend")
            lifeline_choice = input("Choose an option: \n")
            if lifeline_choice == "1":
                print("You've selected 50/50 - Computer, please take away two random wrong answers!")
                fifty_fifty_lifeline = lifeline.Lifeline()
                take_away_two = fifty_fifty_lifeline.fifty_fifty(question, correct_answer, name)
                print(take_away_two)
            

            if lifeline_choice == "2":
                print("You want to ask the audience! Audience, please select A, B, C or D")
                # Run code to randomise answer selection from sample of 100
                # Correct answer = 60-90%?
                # Incorrect answer = 15-55%?

            if lifeline_choice == "3":
                print("You want to call a friend? We'll call them now?")
                print("Hey" + self.name + ", the answer is " + correct_answer)

        if option == "3":
            print("You want to take the money? Are you sure?")
            confirm_take = input("Yes or No? ")
            # if confirm_take == "Yes":
            #     return "Interesting choice! Thank you for playing! You go away with {cash_prize}".format(cash_prize = self.cash_prize)
            # else:
                


                

    