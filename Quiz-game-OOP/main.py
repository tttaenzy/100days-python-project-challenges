from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    text_question = item["text"]
    answer_question = item["answer"]
    new_question = Question(text_question, answer_question)
    question_bank.append(new_question)

q1 = QuizBrain(question_bank)
while q1.still_has_question():
    q1.next_question()

print("You've completed the quiz")
print(f"Your final score was: {q1.score}/{len(question_bank)}")
