class QuizBrain:
    def __init__(self, questions_list):
        self.questions_list = questions_list
        self.question_number = 0
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def next_question(self):
        x = input(
            f"Q.{self.question_number + 1}: {self.questions_list[self.question_number].text} (True/False)?").lower()
        return x

    def ck_answer(self, x):
        if (self.questions_list[self.question_number].answer == "True" and x == "true") or (self.questions_list[self.question_number].answer == "False" and x == "false"):
            self.score += 1
            self.question_number += 1
            print(f"Right you got it your score is {self.score}")
        else:
            print(f"wrong sorry, your current score is {self.score}")
