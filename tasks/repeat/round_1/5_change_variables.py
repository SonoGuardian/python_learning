# 5. Перестановка переменных
# Есть переменные:
# a = 5
# b = 7
# Поменяй их значения местами без использования временной переменной.
#======================


def changing(first,second):
    print("Let's change them")
    first, second = second, first
    print (f"The first one: {first}") 
    print (f"The second one: {second}") 


a_number = input("Enter first number: ")
b_number = input("Enter second number: ")
changing(a_number, b_number)
