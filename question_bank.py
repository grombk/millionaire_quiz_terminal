import random

class QuestionBank:
    questions_asked = []

    questions_answers = {
        "In which part of your body would you find the cruciate ligament?": ["Elbow", "Ankle", "Knee", "Hip"],
        "What is the name of the main antagonist in the Shakespeare play Othello?": ["Iago", "Cassio", "Roderigo", "Brabantio"],
        "What element is denoted by the chemical symbol Sn in the periodic table?": ["Sodium", "Tin", "Gold", "Phosphorus"],
        "How many of Henry VIII’s wives were called Catherine?": ["2", "3", "4", "5",],
        "In what US State is the city Nashville?": ["Texas", "Washington", "Tennessee", "Ohio"],
        "What is the currency of Denmark?": ["Krone", "Florin", "Euro", "Kuna"],
        "Which Tennis Grand Slam is played on a clay surface?": ["The US Open", "Wimbledon", "The French Open", "The Australian Open"],
        "In which European country would you find the Rijksmuseum?": ["Belgium", "Germany", "Switzerland", "The Netherlands"],
        "How many films have Al Pacino and Robert De Niro appeared in together?": ["2", "3", "4", "5"],
        "What is the smallest planet in our solar system?": ["Mercury", "Uranus", "Neptune", "Venus"],
        "Which legendary surrealist artist is famous for painting melting clocks?": ["Vincent Van Gogh", "Salvador Dali", "Pablo Picasso", "Claude Monet"]
    }

    questions_correct_answers = {
        "In which part of your body would you find the cruciate ligament?": "C",
        "What is the name of the main antagonist in the Shakespeare play Othello?": "A",
        "What element is denoted by the chemical symbol Sn in the periodic table?": "B",
        "How many of Henry VIII’s wives were called Catherine?": "B",
        "In what US State is the city Nashville?": "C",
        "What is the currency of Denmark?": "A",
        "Which Tennis Grand Slam is played on a clay surface?": "C",
        "In which European country would you find the Rijksmuseum?": "D",
        "How many films have Al Pacino and Robert De Niro appeared in together?": "C",
        "What is the smallest planet in our solar system?": "A",
        "Which legendary surrealist artist is famous for painting melting clocks?": "B"
    }

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
        "C",
        "A",
        "B",
        "B",
        "C",
        "A",
        "C",
        "D",
        "C",
        "A",
        "B"
    ]

    def __init__(self, questions_and_answers, correct_answers):
        self.questions_answers = questions_and_answers
        self.correct_answers = correct_answers

    def choose_question(self, questions_and_answers):
        shuffled_list = list(questions_and_answers.items())
        random.shuffle(shuffled_list)
        new_list = dict(shuffled_list)
        for question in new_list.keys():
            if question not in self.questions_asked:
                self.questions_asked.append(question)
                return question

    def get_answers_for_question(self, question):
        answers = self.questions_answers[question]
        return "\nA: {answers[0]}  B:  {answers[1]}  C:  {answers[2]}  D:  {answers[3]}\n".format(answers=answers)

    def get_correct_answer(self, question):
        correct_answer = self.questions_correct_answers[question]
        return correct_answer
            

    

    

        
            