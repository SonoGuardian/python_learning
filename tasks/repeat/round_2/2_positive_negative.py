#2. Определение знака числа
#Пусть программа определяет, положительное, отрицательное или ноль введено.
#=========================



def determitane(number):
    try:
        number = int(number)
        if number == 0:
            print("It 0, we didn't handle zero here")
        elif number >=0:
            print(f"{number} is positive")
        elif number <=0:
            print(f"{number} is negative")
    except ValueError:
        print("I know what's your doing. This is not a number")

    
user_number = input("Enter number to determinate is it positive or negative: ")
determitane(user_number)