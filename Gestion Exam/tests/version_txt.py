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