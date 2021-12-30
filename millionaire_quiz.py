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

# Select the first question to ask
question_to_ask = question.choose_question(question.questions)

# Get the answers for the question
answers_to_question = question.get_answers_for_question(question_to_ask, question.answers)

# Get correct answer for question
correct_answer = question.get_correct_answer(question_to_ask)

print(question_to_ask)
print(answers_to_question)

print(player.answer_choice())




