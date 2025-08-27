# 8. Пропуск числа
# Выведи числа от 1 до 10, но пропусти 5 (используй continue).
#================================

# for i in range(1,11):
#     print(i)
#     if i == 5

# i=1
# while i < 11:
#     for i in range(1,11):
#         if i == 5:
#             continue
#         print(i)
#         i +=1 
#------------------alt-----------------
for i in range(1, 11):
    if i == 5:
        continue  # Пропускаем число 5
    print(i)