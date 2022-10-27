
spisok = []
for i in range(1, 100):
    if i % 3 != 0:

        continue
    spisok.append(i)
else:
    print(spisok)

# i = 0
# while i <= 100:
#     i += 1
#     if i % 2 == 0 and i != 0:
#         continue
#     print(i)

# i = 0
# while i <= 100:
#     i += 1
#     if i % 2 == 0 and i != 0:
#         break
#     print(i)

# aman_zadanie = ['pin', 'stul']
# counter = 0
# while True:
#     if counter == 3:
#         aman_zadanie.clear()
#         print(f'Количество попыток исчерпано. Вы удалены из системы! {aman_zadanie}')
#         break
#     login = input('Введите логин: ')
#     password = input('Введите пароль: ')
#     if login == aman_zadanie[0] and password == aman_zadanie[1]:
#         print('Вы вошли в систему')
#         break
#     elif counter < 3:
#          counter = counter + 1
#          if counter <= 2:
#              print('Повторно введите логин и пароль')

# def check_if_exists(arr)-> bool:
#     i = 0
#     j = 1
#     for i in range(len(arr)):
#         for j in range(len(arr)):
#             if arr[i] == 2 * arr[j] or arr[i] == arr[j] / 2:
#                 return True
#             else:
#                 return False
#
# result = check_if_exists([10, 5, 7, 2, 3])
# print(result)
#




