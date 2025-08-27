# 7. Счётчик попыток
# Добавь к предыдущей задаче ограничение: максимум 3 попытки ввода пароля, после чего выводить “Доступ заблокирован”.
#=========================

access_passowd='1234qwer'

def password_ckecking ():
    i=0
    while i <= 3:
        user_password=input('Enter the password:')
        if user_password == access_passowd:
            print ("Access allowed")
            print ()
            break
        else:
            print ("Access Denied")
            print ()
            i += 1
            if i > 3:
                print ("Access blocked")
                print ()


#user_pass=input('Enter the password:')
password_ckecking()