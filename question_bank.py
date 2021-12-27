import random

class QuestionBank:
    questions = {
        1: "In which part of your body would you find the cruciate ligament?",
        2: "What is the name of the main antagonist in the Shakespeare play Othello?",
        3: "What element is denoted by the chemical symbol Sn in the periodic table?",
        4: "How many of Henry VIII’s wives were called Catherine?",
        5: "In what US State is the city Nashville?",
        6: "What is the currency of Denmark?",
        7: "Which Tennis Grand Slam is played on a clay surface?",
        8: "In which European country would you find the Rijksmuseum?",
        9: "How many films have Al Pacino and Robert De Niro appeared in together?",
        10: "What is the smallest planet in our solar system?",
        11: "Which legendary surrealist artist is famous for painting melting clocks?"
    }

    answers = {
        1: ["Elbow", "Ankle", "Knee", "Hip"],
        2: ["Iago", "Cassio", "Roderigo", "Brabantio"],
        3: ["Sodium", "Tin", "Gold", "Phosphorus"],
        4: ["2", "3", "4", "5",],
        5: ["Texas", "Washington", "Tennessee", "Ohio"],
        6: ["Krone", "Florin", "Euro", "Kuna"],
        7: ["The US Open", "Wimbledon", "The French Open", "The Australian Open"],
        8: ["Belgium", "Germany", "Switzerland", "The Netherlands"],
        9: ["2", "3", "4", "5"],
        10: ["Mercury", "Uranus", "Neptune", "Venus"],
        11: ["Vincent Van Gogh", "Salvador Dali", "Pablo Picasso", "Claude Monet"]
    }

    correct_answers = {
        1: "Knee",
        2: "Iago",
        3: "Tin",
        4: "3",
        5: "Tennessee",
        6: "Krone",
        7: "The French Open",
        8: "The Netherlands",
        9: "4",
        10: "Mercury",
        11: "Salvador Dali"
    }

    def __init__(self, question_list, answer_list, correct_answer_list):
        self.question_list = question_list
        self.answer_list = answer_list
        self.correct_answer_list = correct_answer_list

    def choose_question(self, question_list):
        questions_asked = []
        question = question_list[random.randint(1, len(question_list))]
        questions_asked.append(question)
        if question not in questions_asked:
            return question

        
            