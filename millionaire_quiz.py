import player
import question_bank

print("""
##       ## ###### ####   ####   ###### ###### ##     ## ######
####    ###   ##   ##     ##       ##   ##  ## ###    ## ##
## ## ## ##   ##   ##     ##       ##   ##  ## ## #   ## ###
##  ##   ##   ##   ##     ##       ##   ##  ## ##  #  ##  ###
##       ##   ##   ##     ##       ##   ##  ## ##   # ##   ###
##       ##   ##   ##   # ##   #   ##   ##  ## ##    ###    ###
##       ## ###### ###### ###### ###### ###### ##    ### ######
""")
print("============================================================")
print("Welcome to Millions! A quiz game where you can walk away with £1,000,000!")
print("============================================================")
player_name = input("Please enter your name to start: ")
print("============================================================")
# Instantiate Player Class
player = player.Player(player_name)

# Greet Player
print(player.greeting(player_name))
# Instantiate QuestonBank Class
question = question_bank.QuestionBank(question_bank.QuestionBank.questions, question_bank.QuestionBank.answers, question_bank.QuestionBank.correct_answers)

# Question 1
print("=== Question 1 ===")
question_1 = question.choose_question(question.questions)
print(question_1)
answers_to_question_1 = question.get_answers_for_question(question_1, question.answers)
print(answers_to_question_1)
correct_answer_question_1 = question.get_correct_answer(question_1)
print(player.answer_choice(correct_answer_question_1))

# Question 2
print("=== Question 2 ===")
question_2 = question.choose_question(question.questions)
print(question_2)
answers_to_question_2 = question.get_answers_for_question(question_2, question.answers)
print(answers_to_question_2)
correct_answer_question_2 = question.get_correct_answer(question_2)
print(player.answer_choice(correct_answer_question_2))

# Question 3
print("\n=== Question 3 ===")
question_3 = question.choose_question(question.questions)
print(question_3)
answers_to_question_3 = question.get_answers_for_question(question_3, question.answers)
print(answers_to_question_3)
correct_answer_question_3 = question.get_correct_answer(question_3)
print(player.answer_choice(correct_answer_question_3))

# Question 4
print("=== Question 4 ===")
question_4 = question.choose_question(question.questions)
print(question_4)
answers_to_question_4 = question.get_answers_for_question(question_4, question.answers)
print(answers_to_question_4)
correct_answer_question_4 = question.get_correct_answer(question_4)
print(player.answer_choice(correct_answer_question_4))

# Question 5
print("=== Question 5 ===")
question_5 = question.choose_question(question.questions)
print(question_5)
answers_to_question_5 = question.get_answers_for_question(question_5, question.answers)
print(answers_to_question_5)
correct_answer_question_5 = question.get_correct_answer(question_5)
print(player.answer_choice(correct_answer_question_5))

# Question 6
print("=== Question 6 ===")
question_6 = question.choose_question(question.questions)
print(question_6)
answers_to_question_6 = question.get_answers_for_question(question_6, question.answers)
print(answers_to_question_6)
correct_answer_question_6 = question.get_correct_answer(question_6)
print(player.answer_choice(correct_answer_question_6))

# Question 7
print("=== Question 7 ===")
question_7 = question.choose_question(question.questions)
print(question_7)
answers_to_question_7 = question.get_answers_for_question(question_7, question.answers)
print(answers_to_question_7)
correct_answer_question_7 = question.get_correct_answer(question_7)
print(player.answer_choice(correct_answer_question_7))

# Question 8
print("=== Question 8 ===")
question_8 = question.choose_question(question.questions)
print(question_8)
answers_to_question_8 = question.get_answers_for_question(question_8, question.answers)
print(answers_to_question_8)
correct_answer_question_8 = question.get_correct_answer(question_8)
print(player.answer_choice(correct_answer_question_8))

# Question 9
print("=== Question 9 ===")
question_9 = question.choose_question(question.questions)
print(question_9)
answers_to_question_9 = question.get_answers_for_question(question_9, question.answers)
print(answers_to_question_9)
correct_answer_question_9 = question.get_correct_answer(question_9)
print(player.answer_choice(correct_answer_question_9))

# Question 10
print("=== Question 10 ===")
question_10 = question.choose_question(question.questions)
print(question_10)
answers_to_question_10 = question.get_answers_for_question(question_10, question.answers)
print(answers_to_question_10)
correct_answer_question_10 = question.get_correct_answer(question_10)
print(player.answer_choice(correct_answer_question_10))

# Question 11
print("=== Question 11 ===")
question_11 = question.choose_question(question.questions)
print(question_11)
answers_to_question_11 = question.get_answers_for_question(question_11, question.answers)
print(answers_to_question_11)
correct_answer_question_11 = question.get_correct_answer(question_11)
print(player.answer_choice(correct_answer_question_11))