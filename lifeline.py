import player
import question_bank
import random

class Lifeline:
    fifty_fifty = True
    ask_the_audience = True
    call_a_friend = True

    def get_wrong_letter_answer(self, question, random_wrong_answer):
        answers_to_question = question_bank.QuestionBank.questions_answers[question]
        
        letter_answer = ""
        if random_wrong_answer == answers_to_question[0]:
            letter_answer += "A"
        elif random_wrong_answer == answers_to_question[1]:
            letter_answer += "B"
        elif random_wrong_answer == answers_to_question[2]:
            letter_answer += "C"
        elif random_wrong_answer == answers_to_question[3]:
            letter_answer += "D"

        return letter_answer

    def fifty_fifty(self, question, correct_answer, name):
        # Get the answers for the question being asked
        answers_to_question = question_bank.QuestionBank.questions_answers[question]
        copy_of_answers = answers_to_question
        answer_question = player.Player(name)
        # Get the correct answer and three wrong answers
        # Randomly choose a wrong answer from incorrect list
        if correct_answer == "A":
            correct = copy_of_answers[0]
            copy_of_answers.remove(correct)
            random_one_wrong = random.choice(copy_of_answers)
            wrong_letter_answer = self.get_wrong_letter_answer(question, random_one_wrong)
            Lifeline.fifty_fifty = False
            print("A: {correct} {wrong_letter_answer}: {random_one_wrong}\n".format(correct=correct, wrong_letter_answer=wrong_letter_answer, random_one_wrong=random_one_wrong))
            print(answer_question.answer_choice(question, correct_answer, name))
        elif correct_answer == "B":
            correct = copy_of_answers[1]
            copy_of_answers.remove(correct)
            random_one_wrong = random.choice(copy_of_answers)
            wrong_letter_answer = self.get_wrong_letter_answer(question, random_one_wrong)
            Lifeline.fifty_fifty = False
            print("B: {correct} {wrong_letter_answer}: {random_one_wrong}\n".format(correct=correct, wrong_letter_answer=wrong_letter_answer, random_one_wrong=random_one_wrong))
            print(answer_question.answer_choice(question, correct_answer, name))
        elif correct_answer == "C":
            correct = copy_of_answers[2]
            copy_of_answers.remove(correct)
            random_one_wrong = random.choice(copy_of_answers)
            wrong_letter_answer = self.get_wrong_letter_answer(question, random_one_wrong)
            Lifeline.fifty_fifty = False
            print("C: {correct} {wrong_letter_answer}: {random_one_wrong}\n".format(correct=correct, wrong_letter_answer=wrong_letter_answer, random_one_wrong=random_one_wrong))
            print(answer_question.answer_choice(question, correct_answer, name))
        elif correct_answer == "D":
            correct = copy_of_answers[3]
            copy_of_answers.remove(correct)
            random_one_wrong = random.choice(copy_of_answers)
            wrong_letter_answer = self.get_wrong_letter_answer(question, random_one_wrong)
            Lifeline.fifty_fifty = False
            print("D: {correct} {wrong_letter_answer}: {random_one_wrong}\n".format(correct=correct, wrong_letter_answer=wrong_letter_answer, random_one_wrong=random_one_wrong))
            print(answer_question.answer_choice(question, correct_answer, name))
    
