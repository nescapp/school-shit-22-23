"""
make a python program that would interpret the following .txt file (stored as "QCM.txt" in the same directory as the .py file) and would proceed to ask each question and listing all answers with a corresponding letter (A,B,C,D) and letting the user choose an answer. It would then say if the answer is correct or not. In the .txt file, the questions are written first and under them would be listed all responses with a "-" followed by "x' if it is a wrong answer and ">" if it is a correct answer. The question ends with an empty line. This is the .txt file:
Quelle est la capitale de la France ?
-> Paris
-x Marseille
-x Lyon
-x Toulouse

Quelle est la capitale de l'Espagne ?
-x Madrid
-> Barcelone
-x Valence
-x Séville

"""
import os

class question:
    def __init__(self, question, answers, correct_answer_index):
        self.question = question
        self.answers = answers
        self.correct_answer_index = correct_answer_index
    
    def ask(self):
        print(self.question)
        for i, answer in enumerate(self.answers): 
            # for each answer, print a letter (A, B, C, D) and the answer
            print(f"{chr(ord('A') + i)}. {answer}")
        # ask the user for an answer
        user_answer = input("Your answer (A, B, C, or D): ").upper()
        # convert user answer to index (0, 1, 2, or 3)
        user_answer_index = ord(user_answer) - ord('A')
        if user_answer_index == self.correct_answer_index:
            print("Correct!")
        else:
            print("Wrong!")

# test = question("test", ["test1", "test2", "test3", "test4"], 2)
# test.ask()

# for every line that doesn't start with a "-" and is not empty, create a question object
qcm = os.path.join(os.path.dirname(__file__), "QCM.txt")

questions = []
with open(qcm, 'r') as file:
    answers = []
    answer_index = 0
    for line in file:
        if line[0] != "-" and line != "\n":
            question_text = line.strip()
            print("\033[2mdebug: question found\033[0m")
        elif line[0] == "-":
            answer_index += 1
            answers.append(line[1:].strip())
            if line[1] == ">":
                correct_answer_index = answer_index - 1
                print("\033[2mdebug: correct answer added\033[0m")
        elif line == "\n":
            questions.append(question(question_text, answers, correct_answer_index))
            print("\033[2mdebug: question added\033[0m")
            answers = []
            answer_index = 0

for question in questions:
    question.ask()
    print()


