# 1. Список квадратов
# Создай список чисел от 1 до 10 и выведи новый список, где каждый элемент возведён в квадрат.
#======================


# square_list = []

# for i in range(1,11):
#     square_list.append(i)

# print(f'Original list: {square_list}')

# n=0
# for square_num in square_list:
#     square_num= (square_num**2)
#     square_list[n]=square_num
#     n+=1


# print(f'New list: {square_list}')
#------------------

numbers = list(range(1, 11))

squares = [x**2 for x in numbers]

print("Original list:", numbers)
print("New list:", squares)