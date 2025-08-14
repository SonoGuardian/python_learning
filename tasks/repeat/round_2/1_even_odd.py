# 1. Чётное или нечётное
# Запроси число и выведи, чётное оно или нечётное.
# =======================

def checking():
    while True:
        number=input("Enter any number: ")
        try:
            number=int(number)
            if number == 0:
                print("0 is not counting, try again")
                continue
            elif number % 2 == 0:
                print(f"The {number} is Even")
            else:
                print(f"The {number} is Odd")
            break
        except ValueError:
            print("Wrong data. Please try again.")
            




checking()


