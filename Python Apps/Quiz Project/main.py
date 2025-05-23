from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for a in range(len(question_data)):
    question_bank.append(Question(question_data[a]["text"], question_data[a]["answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    x = quiz.next_question()
    quiz.ck_answer(x)
