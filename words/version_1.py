''' Итак, это простая игра на разгадку слов с перепутанным порядком букв.
Сделаем это пока в консоли'''
import random

w = open('word_rus.txt', encoding='utf-8')
for line in w:
    line_list=list(line)
    line_list.remove('\n')
    br = random.sample(line_list,  len(line_list))
    print (br)
    input ()
    print (line)
    w.close
