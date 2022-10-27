# cortej = (1, (2, 5), 'f', (2, 3, 5), ('a', 'b'))
# list2 = list()
#
# for i in cortej:
#     if type(i) == tuple and len(i) % 2 == 0 and len(i) != 0:
#         list2.append(i)
# cortej = tuple(list2)
# print(cortej)

# tuples = (1, (2, 5), 'f', (2, 3, 5))
# tuples_l = list()
# for i in tuples:
#     if type(i) == tuple and len(i) % 2 == 0 and len(i) != 0:
#         tuples_l.append(i)
#
# tuples = tuple(tuples_l)
#
# print(tuples)

stroka = 'Nurlan'
print(stroka.maketrans({'N' : 'n', 'n' : 'N'}))
