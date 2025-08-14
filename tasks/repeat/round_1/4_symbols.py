# 4. Подсчёт символов
# Попроси пользователя ввести слово и выведи:
# количество символов
# первый и последний символ
#===========================

def symbol_counter(sentence):
    print(f"The full length of the string is {len(sentence)}")
    print(f"The length of the string without spaces is {len(sentence) - sentence.count(' ')}")

def first_last(sentence):
    print(f"Fist symbol in string: {sentence[0]}")
    print(f"Last symbol in string: {sentence[-1]}")


user_input = input("Enter any sentence: ")
symbol_counter(user_input)
first_last(user_input)
