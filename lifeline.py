import random
import question_bank

class Lifeline:
    fifty_fifty_ready = True
    ask_the_audience_ready = True
    skip_question_ready = True

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
        if self.fifty_fifty_ready:
            print("\nYou've selected 50/50 - Computer, please take away two random wrong answers!")
            answer_list = question_bank.QuestionBank.questions_answers[question]
            correct_question = self.get_correct_letter_answer(question, correct_answer)
            answer_list.remove(correct_question)
            random_one_wrong = random.choice(answer_list)
            wrong_letter_answer = self.get_wrong_letter_answer(question, random_one_wrong)
            self.fifty_fifty_ready = False
            if correct_answer < wrong_letter_answer:
                return "{correct_answer}: {correct_question} {wrong_letter_answer}: {random_one_wrong}\n".format(correct_question=correct_question, correct_answer=correct_answer, wrong_letter_answer=wrong_letter_answer, random_one_wrong=random_one_wrong)
            else:
                return "{wrong_letter_answer}: {random_one_wrong} {correct_answer}: {correct_question}\n".format(correct_question=correct_question, correct_answer=correct_answer, wrong_letter_answer=wrong_letter_answer, random_one_wrong=random_one_wrong)
            
        else:
            return "\n=== You've already used your 50/50 lifeline! ===\n"

    def ask_the_audience(self, question, correct_answer):
        if self.ask_the_audience_ready:
            print("\nYou've selected Ask the Audience - Audience, please choose A, B, C or D.\n")
            answer_list = question_bank.QuestionBank.questions_answers[question]
            
            percentage_correct = random.randint(55, 96)
            first_perc_wrong = random.randint(1, (100 - percentage_correct))
            second_perc_wrong = random.randint(1, (100 - percentage_correct - first_perc_wrong))
            third_perc_wrong = random.randint(1, (100 - percentage_correct - first_perc_wrong - second_perc_wrong))

            self.ask_the_audience_ready = False

            # Could I create one string variable here and then insert where the correct percentage should go? This would involve shifting the wrong perc around
            if correct_answer == "A":
              return "=== A: {answer_list[0]} ({percentage_correct}%) B: {answer_list[1]} ({first_perc_wrong}%) C: {answer_list[2]} ({second_perc_wrong}%) D: {answer_list[3]} ({third_perc_wrong}%) ===\n".format(answer_list=answer_list, percentage_correct=percentage_correct, first_perc_wrong=first_perc_wrong, second_perc_wrong=second_perc_wrong, third_perc_wrong=third_perc_wrong)
            elif correct_answer == "B":
              return "=== A: {answer_list[0]} ({first_perc_wrong}%) B: {answer_list[1]} ({percentage_correct}%) C: {answer_list[2]} ({second_perc_wrong}%) D: {answer_list[3]} ({third_perc_wrong}%) ===\n".format(answer_list=answer_list, percentage_correct=percentage_correct, first_perc_wrong=first_perc_wrong, second_perc_wrong=second_perc_wrong, third_perc_wrong=third_perc_wrong)
            elif correct_answer == "C":
              return "=== A: {answer_list[0]} ({first_perc_wrong}%) B: {answer_list[1]} ({second_perc_wrong}%) C: {answer_list[2]} ({percentage_correct}%) D: {answer_list[3]} ({third_perc_wrong}%) ===\n".format(answer_list=answer_list, percentage_correct=percentage_correct, first_perc_wrong=first_perc_wrong, second_perc_wrong=second_perc_wrong, third_perc_wrong=third_perc_wrong)
            elif correct_answer == "D":
              return "=== A: {answer_list[0]} ({first_perc_wrong}%) B: {answer_list[1]} ({second_perc_wrong}%) C: {answer_list[2]} ({third_perc_wrong}%) D: {answer_list[3]} ({percentage_correct}%) ===\n".format(answer_list=answer_list, percentage_correct=percentage_correct, first_perc_wrong=first_perc_wrong, second_perc_wrong=second_perc_wrong, third_perc_wrong=third_perc_wrong)

        else:
            return "\n=== You've already used your Ask the Audience lifeline! ===\n"

    def skip_question(self):
        if self.skip_question_ready:
            print("\nYou've selected Skip Question - Let's move on to the next one!")
            self.skip_question_ready = False
        else:
            return "\n=== You've already used your Skip Question lifeline! ===\n"

        
    
