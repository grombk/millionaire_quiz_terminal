import lifeline
import sys

lifelines = lifeline.Lifeline()

class Player:
    cash_prize = 0
    questions_correctly_answered = 0
    game_over = False

    def greeting(self, name):
        return "Welcome {name}! Here is your first question...\n".format(name=name)

    def answer_choice(self, question, correct_answer):
        print("What do you want to do?")
        print("1: Answer")
        print("2: Use Lifeline")
        print("3: Take the Money")
        option = input("Choose an option: \n")
        while option == "1":
            answer = input("What is the answer?: ")
            while answer not in ["A", "B", "C", "D"]:
                print("Please enter A, B, C or D")
                break
            while answer == correct_answer:
                if self.questions_correctly_answered == 0:
                    self.questions_correctly_answered += 1
                    self.cash_prize = 1000
                    return "CORRECT! You are on £1,000\n"
                elif self.questions_correctly_answered and self.cash_prize < 1000000:
                    self.questions_correctly_answered += 1
                    self.cash_prize *= 2
                    return "CORRECT! You are on £{:,}\n".format(self.cash_prize)
                elif self.questions_correctly_answered == 11:
                    return "CORRECT! Congratulations, you have won the top prize of £1,000,000!!!\n"        
            
            else:
                print("You haven't answered correctly, better luck next time! You've won £{:,}!\n".format(self.cash_prize))
                sys.exit()

        
        while option == "2":
            print("Which lifeline would you like to use?")
            print("1: 50/50")
            print("2: Ask the Audience")
            print("3: Skip Question")
            print("4: Go Back")
            
            lifeline_choice = input("Choose an option: \n")
            if lifeline_choice == "1":
                take_away_two = lifelines.fifty_fifty(question, correct_answer)
                print(take_away_two)
                return self.answer_choice(question, correct_answer)
            
            if lifeline_choice == "2":
                audience_answers = lifelines.ask_the_audience(question, correct_answer)
                print(audience_answers)
                return self.answer_choice(question, correct_answer)

            if lifeline_choice == "3":
                print("Skipping question...")
                

        while option == "3":
            print("You want to take the money? Are you sure?")
            confirm_take = input("Yes or No? ")
            # if confirm_take == "Yes":
            #     return "Interesting choice! Thank you for playing! You go away with {cash_prize}".format(cash_prize = self.cash_prize)
            # else:
                


                

    