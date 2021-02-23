''' Тренажер таблицы умножения и других навыков для детей'''
import random
import tkinter as tk
import winsound as ws

print ('Привет! Это тренажер таблицы умножения! Приступим!')
while True:
    x = random.randint(1,10) #задаем первое случайное число 
    y = random.randint(1,10) #задаем второе случайное число
    print ('\n Сколько будет '+str(x)+' х '+str(y))
    a= input ()
    if int(a)==x*y: #если ответ правильный
        print ('Да')
        ws.Beep (3000, 200)
        ws.Beep (6000, 200)
    else:
        print ('Нет') #если ответ неправильный
        ws.Beep (500, 800)
           
