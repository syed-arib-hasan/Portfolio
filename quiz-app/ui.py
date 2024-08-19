from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class quizInterface:

    def __init__(self,quiz_brain:QuizBrain):
         self.quiz=quiz_brain
         self.window=Tk()
         self.window.config(padx=20,pady=20,bg=THEME_COLOR)
         self.window.title("Quizzier")

         self.canvas=Canvas(width=300,height=250,bg="white")
         self.question_text=self.canvas.create_text(150,125,width=288,text="Some text",fill=THEME_COLOR,font=("Arial",20,"italic"))
         self.canvas.grid(row=1,column=0,columnspan=2,padx=20,pady=20)
         self.score=Label(text="Score: 0",bg=THEME_COLOR,fg="white",font=("Arial",12))
         self.score.grid(row=0,column=1,padx=20,pady=20)
         
         logo1=PhotoImage(file="true.png")
         self.right=Button(image=logo1,bg=THEME_COLOR,highlightthickness=0,command=self.truepressed)
         self.right.grid(column=0,row=2,padx=20,pady=20)


         logo2=PhotoImage(file="false.png")
         self.left=Button(image=logo2,bg=THEME_COLOR,highlightthickness=0,command=self.falsepressed)
         self.left.grid(column=1,row=2,padx=20,pady=20)

         self.get_next_question()


         self.window.mainloop()

    def get_next_question(self):
         self.canvas.config(bg="white")
         if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
         else:
             self.canvas.itemconfig(self.question_text,text="That's all for now.")
             self.right.config(state="disabled")
             self.left.config(state="disabled")

    def truepressed(self):
         self.feedback(self.quiz.check_answer("True"))

    def falsepressed(self):
         self.feedback(self.quiz.check_answer("False"))

    def feedback(self,right):
        if right:
            self.canvas.config(bg="green")
        elif not right:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)
         



