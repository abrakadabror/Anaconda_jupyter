user_choice_1 = input(
    str('Graczu numer 1 wybierz jedna z opcji: kamien/papier/nozyce '))
user_choice_2 = input(
    str('Graczu numer 2 wybierz jedna z opcji: kamien/papier/nozyce '))

if user_choice_1 == 'papier' and user_choice_2 == 'kamien' or \
        user_choice_1 == 'kamien' and user_choice_2 == 'nozyce' or  \
        user_choice_1 == 'nozyce' and user_choice_2 == 'papier':
    print('Gracz1 wygral')
elif user_choice_1 == user_choice_2:
    print('remis')
else:
    print('Gracz dwa wygral')


# pojemnik = 4
# pojemnik2 = 5

# if pojemnik == 4 and pojemnik2 == 5:
#     print('dziala')
