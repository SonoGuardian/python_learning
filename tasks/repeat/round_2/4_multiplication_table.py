# 4. Таблица умножения для числа
# Запроси число и выведи таблицу умножения на него от 1 до 10 с помощью цикла for.
#=================================

def table(a):
    print("Multiplication table:")
    for i in range(1,11):
        b=a*i
        print(f"{i}x{a} = {b}")

user_mumber = int(input("Enter number:"))
table(user_mumber)
