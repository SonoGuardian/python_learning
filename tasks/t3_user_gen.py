#Ask the user for their first and last name. Generate a simple username by combining:
#The first 3 letters of their first name
#The last 3 letters of their last name
#All in lowercase

first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')

username = first_name[0:3] + last_name[0:3]
print('')
print('Your username: ', username.lower())