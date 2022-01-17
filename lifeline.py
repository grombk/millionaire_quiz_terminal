import player
import question_bank
import random

class Lifeline:
    fifty_fifty_ready = True
    ask_the_audience_ready = True
    call_a_friend_ready = True

    def get_correct_letter_answer(self, question, correct_answer):
        answers_to_question = question_bank.QuestionBank.questions_answers[question]
        correct_question = ""
        if correct_answer == "A":
            correct_question += answers_to_question[0]
        elif correct_answer == "B":
            correct_question += answers_to_question[1]
        elif correct_answer == "C":
            correct_question += answers_to_question[2]
        elif correct_answer == "D":
            correct_question += answers_to_question[3]
        
        return correct_question

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

    def fifty_fifty(self, question, correct_answer):
        # Initilise Classes
        
        if self.fifty_fifty_ready:
            print("\nYou've selected 50/50 - Computer, please take away two random wrong answers!")
            answers_to_question = question_bank.QuestionBank.questions_answers[question]
            copy_of_answers = answers_to_question

            correct_question = self.get_correct_letter_answer(question, correct_answer)
            copy_of_answers.remove(correct_question)
            random_one_wrong = random.choice(copy_of_answers)
            wrong_letter_answer = self.get_wrong_letter_answer(question, random_one_wrong)
            self.fifty_fifty_ready = False
            if correct_answer < wrong_letter_answer:
                return "{correct_answer}: {correct_question} {wrong_letter_answer}: {random_one_wrong}\n".format(correct_question=correct_question, correct_answer=correct_answer, wrong_letter_answer=wrong_letter_answer, random_one_wrong=random_one_wrong)
            else:
                return "{wrong_letter_answer}: {random_one_wrong} {correct_answer}: {correct_question}\n".format(correct_question=correct_question, correct_answer=correct_answer, wrong_letter_answer=wrong_letter_answer, random_one_wrong=random_one_wrong)
            
            
        else:
            return "\n=== You've already used your 50/50 lifeline! ===\n"

        
    
