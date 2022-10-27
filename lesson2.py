# num = []
# alp = []
# vord = 'ab44k5l'
# for i in vord:
#     if i.isdigit():
#         num.append(i)
#     elif i.isalpha():
#         alp.append(i)
#
# print(num)

#
# dlina = int(input('Dlina '))
# vysota = int(input('Vysota '))
# for i in range(vysota):
#     if i == 0 or i == vysota - 1:
#         print('*' * dlina)
#     else:
#         print(f'*{" " * (dlina - 2)}*')


# def same_lists_elements_check(first_list, second_list):
#     new_list = []
#     for i in first_list:
#         if i in second_list and i not in new_list:
#             new_list.append(i)
#     return new_list
#
#
# result = same_lists_elements_check([0, 1, 1, 3, 5, 11], [0, 2, 1, 1, 4, 6, 11])
# print(result)
#
# def find_annoying_integer(numbers):
#     element = None
#     q_elem = 0
#     for i in numbers:
#         q = numbers.count(i)
#         if q > q_elem:
#             q_elem = q
#             element = i
#     return element
#
# result = find_annoying_integer([1, 2, 23, 12, 1, 1, 1, 23, 23, 2])
# print(result)


# def get_first_midd_last_list_elements(input_list):
#     first = input_list[0]
#     middle = input_list[int(len(input_list) / 2)]
#     last = input_list[-1]
#     return f'a = {input_list} -> первый элемент = {first}, средний элемент = {middle}, ' \
#            f'последний элемент = {last}.'
#
# result = get_first_midd_last_list_elements(['c', 1, 2, 3, 4, 5, 6, 'a'])
# print(result)
#
# def cutlet_check(k, m, n):
#     if k >= n:
#         return m * 2
#     else:
#         return (n // k * m * 2) + (n % k * m * 2)
#
# result = cutlet_check(3, 5, 7)
# print(result)



# def find_duplicate(spisok):
#      for i in spisok:
#         q = spisok.count(i)
#         if q == 2:
#             return i
#
# result = find_duplicate([1, 2, 3, 4, 2])
# print(result)


