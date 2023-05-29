import hashlib
import os
import time

if not os.path.exists('students'):
    os.makedirs('students')
if not os.path.exists('students/eleves.txt'):
    with open('students/eleves.txt', 'w') as f:
        pass

class QCM:
    def __init__(self, number, num_questions, duration, questions):
        self.number = number
        self.num_questions = num_questions
        self.duration = duration
        self.questions = questions

    def save_to_file(self):
        filename = f"QCM{self.number}_{time.strftime('%Y')}.txt"
        with open(filename, "w") as f:
            f.write(f"Number of questions: {self.num_questions}\n")
            f.write(f"Duration: {self.duration} minutes\n")
            for i, question in enumerate(self.questions):
                f.write(f"\nQuestion {i+1}: {question['text']}\n")
                for j, answer in enumerate(question['answers']):
                    f.write(f"{'->' if answer['correct'] else '-'} {answer['text']}\n")

class Student:
    def __init__(self, username, password):
        self.username = username
        self.password = hashlib.sha256(password.encode()).hexdigest()

    def save_to_file(self):
        with open("students/eleves.txt", "a") as f:
            f.write(f"{self.username}:{self.password}\n")

class Exam:
    def __init__(self, qcm_number, student_username):
        self.qcm_number = qcm_number
        self.student_username = student_username
        self.date = time.strftime('%Y-%m-%d %H:%M:%S')
        self.answers = []

    def add_answer(self, question_number, answer_number):
        self.answers.append((question_number, answer_number))

    def save_to_file(self):
        filename = f"{self.student_username}_{self.qcm_number}_{self.date.replace(':', '-').replace(' ', '_')}.txt"
        with open(f"students/{filename}", "w") as f:
            f.write(f"QCM number: {self.qcm_number}\n")
            f.write(f"Date: {self.date}\n")
            for i, answer in enumerate(self.answers):
                f.write(f"Question {answer[0]}: {answer[1]}\n")

def create_qcm():
    number = input("Enter the QCM number: ")
    num_questions = int(input("Enter the number of questions: "))
    duration = int(input("Enter the duration of the QCM in minutes: "))
    questions = []
    for i in range(num_questions):
        text = input(f"Enter the text of question {i+1}: ")
        answers = []
        for j in range(4):
            answer_text = input(f"Enter the text of answer {j+1}: ")
            correct = input(f"Is answer {j+1} correct? (y/n) ").lower() == 'y'
            answers.append({'text': answer_text, 'correct': correct})
        questions.append({'text': text, 'answers': answers})
    qcm = QCM(number, num_questions, duration, questions)
    qcm.save_to_file()
    print(f"QCM {number} saved to file.")

def create_account():
    username = input("Enter the student's username: ")
    password = input("Enter the student's password: ")
    student = Student(username, password)
    student.save_to_file()
    print(f"Account for {username} saved to file.")

def take_test():
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    with open("students/eleves.txt") as f:
        for line in f:
            line = line.strip()  # Strip newline character from end of line
            if line.split(':')[0] == username:
                if line.split(':')[1] == hashed_password:
                    qcms = [f for f in os.listdir() if f.startswith("QCM")]
                    taken_qcms = [f.split('_')[0][3:] for f in os.listdir(f"students") if f.startswith(username)]
                    available_qcms = set(qcms) - set(taken_qcms)
                    if not available_qcms:
                        print("No available QCMs.")
                        return
                    print("Available QCMs:")
                    for qcm in available_qcms:
                        print(qcm)
                    qcm_number = input("Enter the number of the QCM you want to take: ")
                    if f"QCM{qcm_number}_{time.strftime('%Y')}.txt" not in available_qcms:
                        print("Invalid QCM number.")
                        return
                    qcm_file = f"QCM{qcm_number}_{time.strftime('%Y')}.txt"
                    # with open(qcm_file) as f:
                    #     num_questions = int(f.readline().split(':')[1].strip())
                    #     duration = int(f.readline().split(':')[1].strip().split()[0])
                    #     questions = []
                    #     for i in range(num_questions):
                    #         text = f.readline().strip()[2:]
                    #         answers = []
                    #         for j in range(4):
                    #             answer_text = f.readline().strip()[2:]
                    #             correct = f.readline().startswith("->")
                    #             answers.append({'text': answer_text, 'correct': correct})
                    #         questions.append({'text': text, 'answers': answers})
                    #     exam = Exam(qcm_number, username)
                    #     start_time = time.time()
                    #     for i, question in enumerate(questions):
                    #         print(f"\nQuestion {i+1}: {question['text']}")
                    #         for j, answer in enumerate(question['answers']):
                    #             print(f"{j+1}. {answer['text']}")
                    #         answer_number = int(input("Your answer: "))
                    #         exam.add_answer(i+1, answer_number)
                    #         if time.time() - start_time > duration * 60:
                    #             print("Time's up!")
                    #             exam.save_to_file()
                    #             print("Exam saved to file.")
                    #             return
                    #     exam.save_to_file()
                    #     print("Exam saved to file.")
                    #     return
                    print("not implemented yet")
                else:
                    print("Incorrect password.")
                    return
        print("Username not found.")
    

def evaluate_test():
    qcms = [f for f in os.listdir() if f.startswith("QCM")]
    for qcm in qcms:
        qcm_number = qcm.split('_')[0][3:]
        exam_files = [f for f in os.listdir(f"students") if f.startswith(f"_{qcm_number}_")]
        grades = []
        for exam_file in exam_files:
            with open(f"students/{exam_file}") as f:
                num_correct = 0
                num_questions = 0
                for line in f:
                    if line.startswith("Question"):
                        num_questions += 1
                    elif line.startswith("Question"):
                        num_correct += 1
                grade = num_correct / num_questions * 100
                grades.append(grade)
        if grades:
            print(f"QCM {qcm_number}:")
            print(f"Minimum grade: {min(grades)}")
            print(f"Maximum grade: {max(grades)}")
            print(f"Average grade: {sum(grades) / len(grades)}")
        else:
            print(f"No exams taken for QCM {qcm_number}.")

def quit_program():
    print("\033c")
    exit()

def ActionForm(actions):
    while True:
        print("(", end="")
        for key in actions:
            print(f"{key}: {actions[key][0]}", end=", ")
        print("\b\b)")

        choice = input("Action: ")
        if choice in actions:
            actions[choice][1]()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    actions = {
        '1': ('Create a QCM', create_qcm),
        '2': ('Create a student account', create_account),
        '3': ('Take an exam', take_test),
        '4': ('Evaluate exams', evaluate_test),
        'q': ('Quit', quit_program)
    }
    while True:
        print("Are you a 'p'rofessor or an 'e'lève?")
        mode = input("Mode: ")
        if mode == 'p':
            prof_actions = {
                '1': ('Create a QCM', create_qcm),
                '2': ('Create a student account', create_account),
                '3': ('Evaluate exams', evaluate_test),
                'r': ('Return', lambda: None),
                'q': ('Quit', quit_program)
            }
            ActionForm(prof_actions)
        elif mode == 'e':
            eleve_actions = {
                '1': ('Take an exam', take_test),
                'q': ('Quit', quit_program)
            }
            ActionForm(eleve_actions)
        elif mode == 'q':
            quit_program()
        else:
            print("Invalid mode. Please try again.")