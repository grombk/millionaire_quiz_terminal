import random

class QuestionBank:
    questions = [
        "In which part of your body would you find the cruciate ligament?",
        "What is the name of the main antagonist in the Shakespeare play Othello?",
        "What element is denoted by the chemical symbol Sn in the periodic table?",
        "How many of Henry VIII’s wives were called Catherine?",
        "In what US State is the city Nashville?",
        "What is the currency of Denmark?",
        "Which Tennis Grand Slam is played on a clay surface?",
        "In which European country would you find the Rijksmuseum?",
        "How many films have Al Pacino and Robert De Niro appeared in together?",
        "What is the smallest planet in our solar system?",
        "Which legendary surrealist artist is famous for painting melting clocks?"
    ]

    answers = [
        ["Elbow", "Ankle", "Knee", "Hip"],
        ["Iago", "Cassio", "Roderigo", "Brabantio"],
        ["Sodium", "Tin", "Gold", "Phosphorus"],
        ["2", "3", "4", "5",],
        ["Texas", "Washington", "Tennessee", "Ohio"],
        ["Krone", "Florin", "Euro", "Kuna"],
        ["The US Open", "Wimbledon", "The French Open", "The Australian Open"],
        ["Belgium", "Germany", "Switzerland", "The Netherlands"],
        ["2", "3", "4", "5"],
        ["Mercury", "Uranus", "Neptune", "Venus"],
        ["Vincent Van Gogh", "Salvador Dali", "Pablo Picasso", "Claude Monet"]
    ]

    correct_answers = [
        "Knee",
        "Iago",
        "Tin",
        "3",
        "Tennessee",
        "Krone",
        "The French Open",
        "The Netherlands",
        "4",
        "Mercury",
        "Salvador Dali"
    ]

    def __init__(self, question_list, answer_list, correct_answer_list):
        self.question_list = question_list
        self.answer_list = answer_list
        self.correct_answer_list = correct_answer_list

    def choose_question(self, question_list):
        questions_asked = []
        question = question_list[random.randint(1, len(question_list)) - 1]
        questions_asked.append(question)
        return question

    def get_answers_for_question(self, question, answer_list):
        question_number = self.questions.index(question)
        answers = answer_list[question_number]
        return "\n\nA: {answers[0]}  B:  {answers[1]}  C:  {answers[2]}  D:  {answers[3]}\n".format(answers=answers)

    def get_correct_answer(self, question):
        correct_answer = self.correct_answers[self.questions.index(question)]
        return correct_answer
            

    

    

        
            