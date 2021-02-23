import random
while True:
   otvet = random.randint(1,3)
   guess = int(input ("Какое число я загадал от 1 до 3? "))
   if guess == otvet:
      print ("Ты победил! Я загадал число " + str(otvet))
   else:
      print ("Неправильно, я загадал " + str(otvet))
