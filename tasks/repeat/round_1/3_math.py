# 3. Арифметика
# Пусть программа запрашивает два числа и выводит их:
# сумму
# разность
# произведение
# частное
#======================

def math():
    a_number = int((input("Enter first number(integer): ")))
    b_number = int((input("Enter second number(integer): ")))

    print(f"Sum: {a_number + b_number}")
    print(f"Substract: {a_number - b_number}")
    print(f"Mupiply: {a_number * b_number}")
    print(f"Divide: {float(a_number / b_number):.2f}")

math()
