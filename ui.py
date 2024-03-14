import tkinter as tk
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class Quiz_ui:

    def __init__(self,quiz:QuizBrain):
        self.quiz_brain=quiz
        self.window = tk.Tk()
        self.window.title("Quiz game")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.lable=tk.Label(text=f"Score:{self.quiz_brain.score}",bg=THEME_COLOR, font=("Arial",20,"italic"))
        self.lable.grid(row=0,column=1)
        self.canvas = tk.Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas_text = self.canvas.create_text(
            150,
            125,
            width=290,
            text="Text",
            fill=THEME_COLOR,
            font=("Arial",25,"italic"))
        self.canvas.grid(row=1, column=1, columnspan=2, pady=50,padx=20)
        right_image = tk.PhotoImage(file="./images/true.png")
        wrong_image = tk.PhotoImage(file="./images/false.png")
        self.button_correct = tk.Button(image=right_image, highlightthickness=0, highlightbackground=THEME_COLOR,command=self.true_pressed)
        self.button_wrong = tk.Button(image=wrong_image, highlightthickness=0, highlightbackground=THEME_COLOR,command=self.false_pressed)

        self.button_correct.grid(row=2, column=1)
        self.button_wrong.grid(row=2, column=2)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        if self.quiz_brain.still_has_questions():
            self.canvas.config(bg="white")
            self.lable.config(text=f"Score:{self.quiz_brain.score}")
            question = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.canvas_text,text=question)
        else:
            self.canvas.config(bg="white")
            self.lable.config(text=f"Score:{self.quiz_brain.score}")
            self.canvas.itemconfig(self.canvas_text, text=f"You answer to all questions ")
            self.button_correct.config(state="disabled")
            self.button_wrong.config(state="disabled")



    def true_pressed(self):
       answer= self.quiz_brain.check_answer("True")
       self.check(answer)

    def false_pressed(self):
        answer=self.quiz_brain.check_answer("False")
        self.check(answer)

    def check(self,anw):
        if str(anw).lower() == "false":
           self.canvas.config(bg="red")
        elif str(anw).lower() == "true":
            self.canvas.config(bg="green")
        self.window.after(1000,self.next_question)














