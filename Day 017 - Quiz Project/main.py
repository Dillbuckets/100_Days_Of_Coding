from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
# from random import randint

question_bank = []

# for _ in range(1, 4):
#     selection = randint(0, len(question_data) - 1)
#     selected_entry = question_data[selection]
#     converted_entry = Question(selected_entry['text'], selected_entry['answer'])
#     prepared_entry = [converted_entry.question, converted_entry.answer]
#     question_bank.append(prepared_entry)

# for entry in question_data:
#     question = entry["text"]
#     answer = entry["answer"]
#     combination = question, answer
#     question_bank.append(combination)

for entry in question_data:
    question = Question(entry["text"], entry["answer"])
    # question_bank.append(question.text)
    # question_bank.append(question.answer)
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print("You've completed the quiz!")
print(f"Your final score is: {quiz.user_score}/{quiz.question_number}")