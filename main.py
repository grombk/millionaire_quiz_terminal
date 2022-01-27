import quiz.question_bank

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

rounds = 1

while rounds < 13:
    question = quiz.question_bank.QuestionBank(quiz.question_bank.QuestionBank.questions_answers, quiz.question_bank.QuestionBank.questions_correct_answers)
    question.ask_question(player_name, rounds)
    rounds += 1


