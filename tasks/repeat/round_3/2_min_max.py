# 2. Минимум и максимум в списке
# Пусть программа принимает от пользователя 5 чисел, сохраняет их в список и выводит на экран:
# минимальное значение
# максимальное значение
#======================

user_input_list=[]

for i in range(1,6):
    i=int(input(f"Enter {i} number:"))
    user_input_list.append(i)

mini = min(user_input_list)
maxi = max(user_input_list)


print(f"Your list: {user_input_list}")



# for max in user_input_list:
#     if max > maxi:
#         maxi=max

# for min in user_input_list:
#     if min < mini:
#         mini=min

print(f"Minimum: {mini}")
print(f"Maximum: {maxi}")