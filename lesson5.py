# for i in range(1, 10):
#     for j in range(1, 11):
#         print(f'{j} * {i} = {i * j}', end='\t') #tabulation
#     print() #new stroka
#
# # matr = [[3, 2, 1],
# #         [2, 3, 3],
# #         [0, 2, 5]]
# # for i in range(len(matr)):
# #     for j in range(len(matr[i])):
# #         if i != j and i > j:
# #             matr[i][j] = 0
# #         elif i != j and i < j:
# #             matr[i][j] = 1
# #     print(matr[i])
#
import random
cities = ['MOSCOW', 'BISHKEK', 'TASHKENT', 'PEKIN']
city = random.choices(cities)
word = ''.join(city)
word1 = list(word)
word_mask = list(''.join('*' * len(word)))
print(word, word_mask)
counter = 0
while True:
     if counter == 5:
         print('Вы проиграли, хотите продолжить? Y/N ')
         continue_game = input()
         if continue_game.upper() == 'Y':
             counter = 0
         else:
             print('До свидания!')
             break
     symbol= input('Введите букву: ')
     if word.find(symbol.upper()) != - 1:
         print('Есть такая буква:')
         symb_index = word.find(symbol.upper())
         word_mask[symb_index] = symbol.upper()
         print(word_mask)
         if '*' not in word_mask:
             print('Вы выиграли!')
             break
     else:
         counter = counter + 1
         if counter <= 4:
             print('Снова')
