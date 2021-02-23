''' Итак, это простая игра на разгадку слов с перепутанным порядком букв.
Сделаем это уже на основе tkinter. Реализация уже будет отличаться от версии 1.0
Сразу скаже, не знаю как, но после трех дней мучений она вдруг заработала!
p.s. Идею украл, но реализовал сам!'''

from tkinter import *
import random

root = Tk()
root.title("Добро пожаловать в буквы и слова!")
root.geometry('400x300')

with open("word_rus.txt", encoding='utf-8') as w:
    array = [row.strip() for row in w]
    
def zagadka():
    global x
    x=list(random.choice(array))
    y=random.sample(x, len(x))
    text2['text']=y
    return x, y

def otvet():
    text2['text']=x
            
text1 = Label(root, text="Составь слово из букв", font=("Tahoma Bold", 18), width=20, height=3)
text2 = Label(root, text = 'Здесь будет слово', bg = 'white', font=("Tahoma Bold", 14), )
#width=20, height=3)

but = Button(text="Далее", width=10, height=1, bg="white", fg="blue", command=zagadka)
but_otvet = Button(text="Ответ", width=10, height=1, bg="white", fg="blue", command=otvet)
quit = Button(text="НАДОЕЛО", fg="red", command=root.destroy)

quit.pack(side="bottom", expand = 1)
text1.pack()
text2.pack()
but.pack(side="left", expand = 1)
but_otvet.pack(side="right", expand = 1)

root.mainloop()

