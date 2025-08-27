# 10. Мини-игра “Угадай число”
# Сгенерируй случайное число от 1 до 10 (random.randint), дай пользователю 3 попытки угадать.
#===============================

import random

random_number = random.randint(1,10)

n_try = 0

while n_try < 3:
    user_gues=int(input("Try to gues number from 1 to 10:"))
    if user_gues==random_number:
        print(f"Your right! It's {random_number}")
        break
    else:
        
        n_try += 1
        if n_try > 3:
            print ("Out of attempts number")
        else:
            print ("Wrong, try one more time")
            print()

