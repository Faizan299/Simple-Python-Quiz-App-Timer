from datetime import *
from tkinter import *

def counter(times = timedelta(minutes=10)):
 times = times-timedelta(seconds=1)
 time.configure(text=times)
 time.after(800, lambda n=times:counter(n))

 
quiz = Tk()
quiz.geometry('800x400')
quiz.title("Quiz Application")
text_Input=StringVar()
time = Label(quiz,font=('Arial', 20,'bold'))
time.pack()

def ans():
    marks=0
    namee=name.get()
    courses=course.get()
    secc=sec.get()
    if namee=="Faizan":
        marks+=10
    if courses=="IOT":
        marks+=5
    if secc=="C":
        marks+=10
    text_Input.set(str(marks))
        

#Label============================================================================
name=Label(quiz,font=("arial",15),text="What is your Name ?").place(x=10,y=55)
course=Label(quiz,font=("arial",15),text="Your Course name is ?").place(x=10,y=105)
section=Label(quiz,font=("arial",15),text="Your section is ?").place(x=10,y=160)
Marks=Label(quiz,font=("arial",15),text="Scores").place(x=10,y=210)

#Entry=============================================================================
name=Entry(quiz,font=(15))
name.place(x=250,y=60)
course=Entry(quiz,font=(15))
course.place(x=250,y=110)
sec=Entry(quiz,font=(15))
sec.place(x=250,y=160)
score=Entry(quiz,font=(15), textvariable=text_Input)
score.place(x=250,y=210)

#Button=============================================================================
save=Button(quiz,font=("arial",15,'bold'),text="Count",bg="black",fg="white",command=ans).place(x=10,y=270)
counter()
quiz.mainloop()
