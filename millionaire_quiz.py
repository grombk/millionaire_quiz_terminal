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
question = question_bank.QuestionBank(question_bank.QuestionBank.questions_answers, question_bank.QuestionBank.questions_correct_answers)

def quiz_rounds(num):
  print("=== Question {num} ===".format(num=num))
  question_num = question.choose_question(question.questions_answers)
  print(question_num)
  answers_to_question_num = question.get_answers_for_question(question_num)
  print(answers_to_question_num)
  correct_answer_question_num = question.get_correct_answer(question_num)
  print(player.answer_choice(question_num, correct_answer_question_num, player_name))

rounds = 1
while rounds < 11:
    quiz_rounds(rounds)
    rounds += 1


