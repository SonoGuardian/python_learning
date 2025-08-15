# 3. Сравнение двух чисел
# Запроси два числа и выведи, какое больше, или что они равны.
#==================

def comparing(a,b):
    if a==b:
        print("They are equal")
    elif a>b:
        print(f'{a} is biiger then {b}')
    elif a<b:
        print(f'{b} is bigger than {a}')
    else:
        print("Not correct data")


number_a = input("Enter first number:")
number_b = input("Enter second number:")
comparing(number_a,number_b)