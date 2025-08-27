# 6. Пароль с проверкой
# Запроси у пользователя пароль.
# Если он совпадает с заданным в коде, вывести "Доступ разрешён", иначе "Неверный пароль".
#=========================

access_passowd='1234qwer'

def password_ckecking (user_password):
    if user_password == access_passowd:
        print ("Access allowed")
    else:
        print ("Access Denied")


user_pass=input('Enter the password:')
password_ckecking(user_pass)