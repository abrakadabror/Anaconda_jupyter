user_choice_1 = input(
    str('Graczu numer 1 wybierz jedna z opcji: kamien/papier/nozyce '))
user_choice_2 = input(
    str('Graczu numer 2 wybierz jedna z opcji: kamien/papier/nozyce '))

if user_choice_1 == 'papier':
    if user_choice_2 == 'kamien':
        print('Gracz1 wygral')
elif user_choice_1 == 'kamien':
    if user_choice_2 == 'nozyce':
        print('Gracz1 wygral')
elif user_choice_1 == 'nozyce':
    if user_choice_2 == 'papier':
        print('Gracz1 wygral')
