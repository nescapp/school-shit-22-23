import xml.etree.ElementTree as ET

# Load XML data from file
xml_file = 'Gestion Exam/tests/QCM.xml'
try:
    tree = ET.parse(xml_file)
    root = tree.getroot()
except FileNotFoundError:
    print(f"Error: '{xml_file}' not found.")
    exit()

# Process each question
for i, question in enumerate(root.findall('question')):
    # Extract the question text
    question_text = question.text.strip()
    print(f'{i + 1}. {question_text}')

    # Extract the answers
    answers = []
    for j, answer in enumerate(question.findall('answer')):
        is_correct = answer.attrib.get('correct') == 'true'
        answer_text = answer.text.strip()
        answers.append((is_correct, answer_text))
        print(f'   {chr(ord("A") + j)}. {answer_text}')

    # Ask the user for an answer
    user_answer = input('Your answer (A, B, C, or D): ').upper()

    # Convert user answer to index (0, 1, 2, or 3)
    user_answer_index = ord(user_answer) - ord('A')

    # Check if the user's answer is correct
    if user_answer_index < len(answers):
        is_correct, correct_answer = answers[user_answer_index]
        if is_correct:
            print('Correct!')
        else:
            print('Faux!')
            print(f'réponse: {correct_answer}')
    else:
        print('erreur!')

    print()
