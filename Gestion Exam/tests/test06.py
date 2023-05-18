import json

# Open the JSON file
with open('Gestion Exam/tests/QCM.json', 'r') as file:
    questions = json.load(file)

# Access the questions
for question in questions:
    print(question['question'])
    for option in question['options']:
        print(option)
    user_answer = input('Enter your answer (A, B, C, or D): ')
    if user_answer.upper() == question['correct_answer']:
        print('Correct!')
    else:
        print('Incorrect!')