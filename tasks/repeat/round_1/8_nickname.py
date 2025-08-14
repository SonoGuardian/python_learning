# 8. Объединение строк
# Пусть программа принимает имя и фамилию, а потом выводит:

# nickname: <[3_first_letters_first_name][3_last_letters_last_name]>

# =====================

def username_creation(first_name, last_name):
    nickname = (first_name[:3].lower() + last_name[-3:].lower())
    nickname2 = (first_name[:3].lower() + last_name[:3].lower())
    print()
    print (f"Your nickname is: {nickname}")
    print (f"Second option: {nickname2}")

f_name = input("Enter your first name: ")
l_name = input("Enter your last name: ")

username_creation(f_name, l_name)