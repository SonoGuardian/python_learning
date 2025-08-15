# 5. Сумма чисел от 1 до N
# Запроси число N и найди сумму всех чисел от 1 до N с помощью while.
#===========================

def find_sum(a):
    i=1
    total=0
    while i <= a:
        total += i
        i += 1

    print(f"Sum from 1 to {a} is {total}")  

user_number = int(input("Enter number:"))
find_sum(user_number)