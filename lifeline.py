import player
import question_bank
import random

class Lifeline:
    fifty_fifty = True
    ask_the_audience = True
    call_a_friend = True

    def fifty_fifty(self, question, correct_answer, name):
        # Get the answers for the question being asked
        answers_to_question = question_bank.QuestionBank.questions_answers[question]
        answer_question = player.Player(name)
        # Get the correct answer and three wrong answers
        # Randomly choose a wrong answer from incorrect list
        if correct_answer == "A":
            correct = answers_to_question[0]
            print(correct)
            answers_to_question.remove(correct)
            random_one_wrong = random.choice(answers_to_question)
            Lifeline.fifty_fifty = False
            print("1: " + correct + " 2: " + random_one_wrong + "\n")
            answer_question.answer_choice(question, correct_answer, name)
        elif correct_answer == "B":
            correct = answers_to_question[1]
            print(correct)
            answers_to_question.remove(correct)
            random_one_wrong = random.choice(answers_to_question)
            Lifeline.fifty_fifty = False
            print("1: " + correct + "2: " + random_one_wrong)
            answer_question.answer_choice(question, correct_answer, name)
        elif correct_answer == "C":
            correct = answers_to_question[2]
            print(correct)
            answers_to_question.remove(correct)
            random_one_wrong = random.choice(answers_to_question)
            Lifeline.fifty_fifty = False
            print("1: " + correct + "2: " + random_one_wrong)
            answer_question.answer_choice(question, correct_answer, name)
        elif correct_answer == "D":
            correct = answers_to_question[3]
            print(correct)
            answers_to_question.remove(correct)
            random_one_wrong = random.choice(answers_to_question)
            Lifeline.fifty_fifty = False
            print("1: " + correct + "2: " + random_one_wrong)
            answer_question.answer_choice(question, correct_answer, name)
    
