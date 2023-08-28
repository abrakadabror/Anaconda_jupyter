# import time
# from time import sleep
# counter = 0
# for nasz_pojemnik in range(10):
#     sleep(1)
#     counter = counter + 1
#     print(nasz_pojemnik, counter)
# print('Kabooom')

# from time import sleep
# for nasz_pojemnik in [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]:
#     sleep(1)
#     print(nasz_pojemnik)
#     if nasz_pojemnik <= 3:
#         sleep(2)
# print('Kaboom')


# from time import sleep
# pojemnik = 4
# if pojemnik == 4:
#     print('w pojemniku jest 5')


# for nasz_pojemnik in range(10):
#     print(nasz_pojemnik)
#     if nasz_pojemnik == 2:
#         sleep(1)
#     if nasz_pojemnik == 1:
#         sleep(1)
#     if nasz_pojemnik == 0:
#         sleep(1)
#     sleep(1)
# print('Kabooom')

# from time import sleep
# for nasz_pojemnik in range(10):
#     print(nasz_pojemnik)
#     if nasz_pojemnik >= 7:
#         sleep(2)
#     else:
#         sleep(1)
# print('Kaboom')

poprawne_opcje = ['kamien', 'papier', 'nozyce']

user_choice = input('Wybierz kamien, papier lub nozyce: ')

if user_choice in poprawne_opcje:
    print('opcja dozwolona')
