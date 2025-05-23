from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class Quiz_ui:
    def __init__(self, question_bank):
        self.quiz = QuizBrain(question_bank)
        self.w = Tk()
        self.w.title("Quizzer App")
        self.w.minsize(width=500, height=500)
        self.w.configure(background=THEME_COLOR)

        self.canvas = Canvas(width=400, height=270)
        self.text = self.canvas.create_text(200, 50, width=350, fill="black", font=("time new roman", 12, "bold"))
        self.canvas.place(x=50, y=50)

        self.label1 = Label(text="Score 0", bg=THEME_COLOR, font=("time new roman", 11, "bold"), fg="white")
        self.label1.place(x=400, y=20)

        def con(color="white"):
            self.canvas.config(bg=color)

        def action1():
            if self.quiz.current_question.answer == "True":
                self.quiz.score += 1
                self.label1.config(text=f"Score {self.quiz.score}")
                con("green")
            elif self.quiz.current_question.answer == "False":
                con("red")
            self.question()
            self.w.after(500, con, "white")

        def action2():
            if self.quiz.current_question.answer == "False":
                self.quiz.score += 1
                self.label1.config(text=f"Score {self.quiz.score}")
                con("green")
            elif self.quiz.current_question.answer == "True":
                con("red")
            self.question()
            self.w.after(500, con, "white")

        true_image = PhotoImage(file="true.png")
        self.button1 = Button(command=action1, image=true_image)
        self.button1.place(x=100, y=350)
        fales_image = PhotoImage(file="false.png")
        self.button2 = Button(command=action2, image=fales_image)
        self.button2.place(x=300, y=350)
        self.question()

        self.w.mainloop()

    def question(self):
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.text, text=self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.text, text="You've completed the quiz")
            self.canvas.itemconfig(self.text,
                                   text=f"Your final score was: {self.quiz.score}/{self.quiz.question_number}")
            self.quiz.current_question.answer = None
